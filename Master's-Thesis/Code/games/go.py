
from copy import deepcopy

###############################
# JUEGO: Go
###############################

# Go es un juego de estrategia para dos jugadores en el que se colocan fichas en un tablero 
# con el objetivo de controlar el mayor territorio al final de la partida.

# Reglas:
# - El juego se juega en un tablero cuadrado con un número impar de filas y columnas entre 5 y 19 (por defecto 9x9)
# - Los jugadores se turnan para colocar fichas de su color (representadas por 1 o 2) en las intersecciones vacías del tablero
# - Una jugada válida debe respetar las reglas de no suicidio y Superko situacional:
#     - Regla de no suicidio: Un jugador no puede colocar una ficha que haga que su propio grupo quede sin libertades
#       inmediatamente, a menos que esa jugada capture fichas enemigas que devuelvan libertades al grupo.
#     - Regla de Superko situacional: Un jugador no puede realizar una jugada que haga que el tablero y el turno
#       actual coincidan exactamente con una situación previa en la misma partida (para evitar ciclos infinitos).
# - Se llaman libertades a las casillas vacías adyacentes a una cierta ficha o grupo de fichas del mismo color
# - Si al colocar una ficha se rodean grupos enemigos sin libertades, estas fichas se capturan y se retiran del tablero
# - Un jugador puede pasar su turno, y si ambos jugadores pasan consecutivamente, el juego termina
# - El puntaje final de cada jugador se calcula sumando:
#     - Las fichas en el tablero de dicho jugador
#     - Las fichas capturadas al oponente
#     - El territorio rodeado exclusivamente por fichas del color de dicho jugador
#     - La compensación Komi de 6.5 puntos para el jugador que no comenzó
# - Gana el jugador con más puntos al final de la partida


class GoGame:
    def __init__(self, rows=9, cols=9, starting_player=1):
        """
        Inicializa el juego

        Parámetros:
        - rows: El número de filas del tablero del juego (por defecto 9, puede tomar valores entre 5 y 19)
        - cols: El número de columnas del tablero del juego (por defecto 9, puede tomar valores entre 5 y 19)
        - starting_player: El jugador que inicia el juego, 1 o -1 (por defecto 1)
        """
        assert 5 <= rows <= 19, "El número de filas debe estar entre 5 y 19."
        assert 5 <= cols <= 19, "El número de columnas debe estar entre 5 y 19."
        assert rows % 2 == 1, "El número de filas debe ser impar."
        assert cols % 2 == 1, "El número de columnas debe ser impar."
        assert rows == cols, "El número de filas y el de columnas deben ser iguales."
        assert starting_player in (1, -1), "El jugador inicial debe ser 1 o -1."

        self.rows = rows
        self.cols = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]  # Definir el tablero
        self.turn = starting_player
        self.eval = []  # Evaluaciones de las simulaciones
        self.pass_count = 0  # Contador de pases consecutivos
        self.history = [(deepcopy(self.board), self.turn)]  # Historial con información de los turnos anteriores

        # Compensación Komi para equilibrar que un jugador juegue primero que el otro
        if starting_player == 1:
            self.count_1 = 0      # Contador de puntos para el jugador 1 (1)
            self.count_2 = 6.5    # Contador de puntos para el jugador 2 (-1)
        elif starting_player == -1:
            self.count_1 = 6.5    # Contador de puntos para el jugador 1 (1)
            self.count_2 = 0      # Contador de puntos para el jugador 2 (-1)


    def comprobar_limites(self, row, col):
        """
        Verifica los límites del tablero
        """
        return 0 <= row < self.rows and 0 <= col < self.cols
    

    def find_group(self, board, row, col, turn):
        """
        Encuentra todas las fichas conectadas al grupo de la ficha colocada en (row, col)
        """
        group = []
        visited = set()
        stack = [(row, col)]  # Comenzamos desde la casilla donde se colocó la ficha

        while stack:
            current_row, current_col = stack.pop()

            if (current_row, current_col) not in visited:
                visited.add((current_row, current_col))
                group.append((current_row, current_col))

                # Revisar las casillas adyacentes
                for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row = current_row + d_row
                    new_col = current_col + d_col

                    if self.comprobar_limites(new_row, new_col) and board[new_row][new_col] == turn:
                        stack.append((new_row, new_col))

        return group


    def has_liberties(self, board, group):
        """
        Verifica si el grupo tiene libertades (casillas vacías adyacentes)
        """
        for row, col in group:

            # Direcciones posibles
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for d_row, d_col in directions:

                # Coordenadas de la casilla adyacente en esa dirección
                new_row = row + d_row
                new_col = col + d_col

                if self.comprobar_limites(new_row, new_col) and board[new_row][new_col] == 0:
                    return True  # Si hay una casilla vacía adyacente, el grupo tiene libertades

        return False  # Si no hay casillas vacías adyacentes, el grupo no tiene libertades
    

    def eliminate_enemy_groups(self, board, row, col, update_score=True):
        """
        Identifica los grupos enemigos adyacentes sin libertades y los elimina del tablero
        """
        # Direcciones posibles
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for d_row, d_col in directions:

            # Coordenadas de la casilla adyacente en esa dirección
            new_row = row + d_row
            new_col = col + d_col

            # Buscar grupos formados por fichas del oponente
            if self.comprobar_limites(new_row, new_col) and board[new_row][new_col] == -self.turn:
                enemy_group = self.find_group(board, new_row, new_col, -self.turn)

                # Si el grupo enemigo no tiene libertades, se elimina
                if not self.has_liberties(board, enemy_group):
                    for enemy_row, enemy_col in enemy_group:
                        board[enemy_row][enemy_col] = 0

                        # Se suman las puntuaciones por fichas enemigas capturadas
                        if update_score:
                            if self.turn == 1:
                                self.count_1 += 1
                            elif self.turn == -1:
                                self.count_2 += 1

        return board


    def valid_actions(self):
        """
        Devuelve una lista con las acciones válidas
        """
        valid_moves = []

        # Se recorren las casillas del tablero
        for row in range(self.rows):
            for col in range(self.cols):

                # Para que una casilla sea válida debe estar vacía
                if self.board[row][col] == 0:

                    # Simular la jugada: colocar la ficha en la casilla seleccionada
                    temp_board = deepcopy(self.board)
                    temp_board[row][col] = self.turn

                    # Eliminar grupos enemigos sin libertades
                    temp_board = self.eliminate_enemy_groups(temp_board, row, col, update_score=False)

                    # Encontrar todas las fichas del grupo asociado a la ficha seleccionada
                    group = self.find_group(temp_board, row, col, self.turn)

                    # Regla del suicidio: Comprobar si el grupo tiene libertades (si no las tiene, el movimiento no es válido)
                    if self.has_liberties(temp_board, group):

                        # Regla de Situational Superko
                        superko = False
                        for (prev_board, prev_turn) in self.history:
                            if temp_board == prev_board and self.turn == prev_turn:
                                superko = True
                                break

                        # Si no se infrinje la regla de Situational Superko
                        if not superko:
                            valid_moves.append((row, col))

        # En Go siempre se puede pasar, así que se añade como acción válida
        valid_moves.append(None)
                                                        
        return valid_moves
    

    def action(self, coordinates):
        """
        Realiza un turno del juego
        """
        if coordinates is None:
            # Pase: no se coloca ficha ni se modifica el tablero
            new_game = GoGame(self.rows, self.cols, -self.turn)
            new_game.board = deepcopy(self.board)
            new_game.eval = self.eval[:]
            new_game.pass_count = self.pass_count + 1
            new_game.count_1 = self.count_1
            new_game.count_2 = self.count_2

            # Actualizar el historial
            if (new_game.board, -self.turn) not in self.history:
                new_game.history = self.history[:] + [(deepcopy(new_game.board), -self.turn)]
            else:
                new_game.history = self.history[:]

            return new_game

        if coordinates not in self.valid_actions():
            raise ValueError("Acción inválida: la jugada no es legal según las reglas de Go "
                             "(puede ser casilla ocupada, suicidio o Superko).")

        row, col = coordinates

        # Crear una copia del tablero actual para el nuevo juego
        new_board = deepcopy(self.board)
        
        # Colocar la ficha en la casilla seleccionada
        new_board[row][col] = self.turn

        # Eliminar grupos enemigos sin libertades
        new_board = self.eliminate_enemy_groups(new_board, row, col)

        # Devolver un nuevo estado del juego con los valores actualizados
        new_game = GoGame(self.rows, self.cols, -self.turn)
        new_game.board = new_board    # Asignar el nuevo tablero
        new_game.eval = self.eval[:]  # Copiar el historial de evaluaciones
        new_game.pass_count = 0       # Reiniciar contador de pases
        new_game.count_1 = self.count_1
        new_game.count_2 = self.count_2

        # Actualizar el historial
        if (new_board, -self.turn) not in self.history:
            new_game.history = self.history[:] + [(deepcopy(new_board), -self.turn)]
        else:
            new_game.history = self.history[:]

        return new_game


    def terminal(self):
        """
        Devuelve True si el juego ha terminado: cuando ambos jugadores han pasado de forma consecutiva
        """
        return self.pass_count >= 2
    

    def evaluate_territory(self, row, col, visited):
        """
        Explora la región vacía conectada a (row, col) y determina si pertenece a un solo jugador
        """
        stack = [(row, col)]
        territory = []
        border_players = set()

        while stack:
            row, col = stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            territory.append((row, col))

            # Revisar vecinos
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for d_row, d_col in directions:
                n_row = row + d_row
                n_col = col + d_col

                if not self.comprobar_limites(n_row, n_col):
                    # El territorio toca el borde del tablero: neutral
                    border_players.add(0)
                    continue

                if self.board[n_row][n_col] == 0:
                    # Casilla vacía, agregar para explorar
                    if (n_row, n_col) not in visited:
                        stack.append((n_row, n_col))
                else:
                    # Casilla con piedra negra (1) o blanca (-1)
                    border_players.add(self.board[n_row][n_col])

        # Si el territorio está rodeado solo por un color (no 0 ni ambos)
        if len(border_players) == 1:
            owner = border_players.pop()
        else:
            owner = 0  # Neutral o compartido

        return territory, owner

    def winner(self):
        """
        Devuelve el ganador: 1 para el jugador 1, -1 para el jugador 2
        """
        # Si no ha acabado el juego, no hay ganador
        if not self.terminal():
            return 0
        
        visited = set()

        count_1_territory = 0
        count_2_territory = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 1:
                    count_1_territory += 1
                elif self.board[row][col] == -1:
                    count_2_territory += 1
                elif self.board[row][col] == 0 and (row, col) not in visited:
                    territory, owner = self.evaluate_territory(row, col, visited)
                    if owner == 1:
                        count_1_territory += len(territory)
                    elif owner == -1:
                        count_2_territory += len(territory)

        final_score_1 = self.count_1 + count_1_territory
        final_score_2 = self.count_2 + count_2_territory

        # Determinar el ganador
        if final_score_1 > final_score_2:
            return 1    # Gana el jugador 1
        elif final_score_1 < final_score_2:
            return -1   # Gana el jugador 2
        elif final_score_1 == final_score_2:
            return 0    # Empate


    def draw(self):
        """
        Dibuja el estado actual del juego
        """
        player = {0: 0, 1: 1, -1: 2}
        for row in self.board:
            player_row = []
            for i in row:
                player_row.append(player[i])
            print(player_row)