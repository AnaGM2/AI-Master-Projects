
###############################
# JUEGO: Othello
###############################

# Othello es un juego de estrategia para dos jugadores en el que se colocan fichas en un tablero 
# con el objetivo de tener la mayoría al final de la partida.

# Reglas:
# - El juego clásico se juega en un tablero de 8x8 casillas (aunque en esta implementación pueden tomar valores entre 4 y 10)
# - Cada ficha tiene una cara blanca y una negra (en esta implementación se representan con 1 y 2).
# - Comienza el jugador que lleva las fichas negras.
# - Los jugadores se turnan para colocar una ficha con su color hacia arriba
# - Una jugada válida debe encerrar una o más fichas del oponente entre la nueva ficha y otra del mismo color
# - Las fichas del oponente que quedan encerradas se voltean al color del jugador que hizo la jugada
# - El juego termina cuando ningún jugador puede hacer una jugada válida
# - Gana quien tenga más fichas de su color en el tablero al final de la partida


class OthelloGame:
    def __init__(self, rows=8, cols=8, starting_player=1):
        """
        Inicializa el juego

        Parámetros:
        - rows: El número de filas del tablero del juego (por defecto 8, puede tomar valores entre 4 y 10)
        - cols: El número de columnas del tablero del juego (por defecto 8, puede tomar valores entre 4 y 10)
        - starting_player: El jugador que inicia el juego, 1 o -1 (por defecto 1)
        """
        assert 4 <= rows <= 10, "El número de filas debe estar entre 4 y 10."
        assert 4 <= cols <= 10, "El número de columnas debe estar entre 4 y 10."
        assert rows % 2 == 0, "El número de filas debe ser par."
        assert cols % 2 == 0, "El número de columnas debe ser par."
        assert starting_player in (1, -1), "El jugador inicial debe ser 1 o -1."

        self.rows = rows
        self.cols = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]  # Definir el tablero

        # Fichas iniciales en el centro
        self.board[rows // 2 - 1][cols // 2 - 1] = -starting_player  # Blanca
        self.board[rows // 2 - 1][cols // 2] = starting_player  # Negra
        self.board[rows // 2][cols // 2 - 1] = starting_player  # Negra
        self.board[rows // 2][cols // 2] = -starting_player  # Blanca

        self.turn = starting_player
        self.eval = []  # Evaluaciones de las simulaciones


    def comprobar_limites(self, row, col):
        """
        Verifica los límites del tablero
        """
        return 0 <= row < self.rows and 0 <= col < self.cols


    def fichas_a_voltear_en_direccion(self, row, col, d_row, d_col):
        """
        Devuelve una lista de fichas que se deben voltear en una dirección dada
        """
        fichas_a_voltear = []

        # Coordenadas de la siguiente casilla en esa dirección
        new_row = row + d_row
        new_col = col + d_col
                
        # Seguir en esa dirección mientras las casillas sigan ocupadas por el oponente
        while self.comprobar_limites(new_row, new_col) and self.board[new_row][new_col] == - self.turn:
            fichas_a_voltear.append((new_row, new_col))

            # Coordenadas de la siguiente casilla en esa dirección
            new_row += d_row
            new_col += d_col

        # Comprobar si hay una ficha del propio jugador que cierra la secuencia
        if self.comprobar_limites(new_row, new_col) and self.board[new_row][new_col] == self.turn:
            return fichas_a_voltear
        else:
            return []  # No se puede voltear nada en esta dirección


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

                    # Direcciones posibles
                    directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (-1,1), (1,1)]
                    for (d_row, d_col) in directions:

                        # Coordenadas de la siguiente casilla en esa dirección
                        new_row = row + d_row
                        new_col = col + d_col

                        # Verificar los límites del tablero
                        if self.comprobar_limites(new_row, new_col):

                            # Comprobar que la primera casilla en esa dirección está ocupada por el oponente
                            if self.board[new_row][new_col] == - self.turn:
                                
                                # Avanzar a la siguiente casilla en esa dirección
                                new_row += d_row
                                new_col += d_col
                                
                                # Seguir en esa dirección mientras las casillas sigan ocupadas por el oponente
                                while self.comprobar_limites(new_row, new_col) and self.board[new_row][new_col] == - self.turn:
                                    new_row += d_row
                                    new_col += d_col

                                # Comprobar que la siguiente casilla en esa dirección esté ocupada por el propio jugador
                                if self.comprobar_limites(new_row, new_col) and self.board[new_row][new_col] == self.turn:
                                    valid_moves.append((row, col))
                                    break

        return valid_moves
    

    def action(self, coordinates):
        """
        Realiza un turno del juego
        """
        if coordinates not in self.valid_actions():
            raise ValueError(f"Acción inválida: la ficha debe colocarse en una casilla vacía de modo que capture "
                             "al menos una ficha del oponente")
        
        row, col = coordinates

        # Crear una copia del tablero actual para el nuevo juego
        new_board = [row[:] for row in self.board]
        
        # Colocar la ficha en la casilla seleccionada
        new_board[row][col] = self.turn

        # Direcciones posibles
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (-1,1), (1,1)]
        for (d_row, d_col) in directions:
            fichas_a_voltear = self.fichas_a_voltear_en_direccion(row, col, d_row, d_col)
            for f_row, f_col in fichas_a_voltear:
                new_board[f_row][f_col] = self.turn  # Voltear la ficha

        # Devolver un nuevo estado del juego con los valores actualizados
        new_game = OthelloGame(self.rows, self.cols, -self.turn)
        new_game.board = new_board    # Asignar el nuevo tablero
        new_game.eval = self.eval[:]  # Copiar el historial de evaluaciones

        # Comprobar si el nuevo jugador puede jugar
        if not new_game.valid_actions():

            # Si no puede, comprobar si el jugador actual sí podía seguir jugando
            if self.valid_actions():
                new_game.turn = self.turn  # El turno no cambia
            
            # Si el jugador actual tampoco tiene jugadas válidas
            else:  
                new_game.turn = -self.turn  # Pasar el turno al oponente

        return new_game


    def terminal(self):
        """
        Devuelve True si el juego ha terminado
        """
        if self.valid_actions():
            return False  # El jugador actual puede jugar

        # Simular el turno del oponente y ver si él puede jugar
        temp_game = OthelloGame(self.rows, self.cols, -self.turn)
        temp_game.board = [row[:] for row in self.board]

        # Si el oponente tampoco tiene jugadas válidas, termina el juego
        if not temp_game.valid_actions():
            return True
        else:
            return False


    def winner(self):
        """
        Devuelve el ganador: 1 para el jugador 1, -1 para el jugador 2
        """
        # Si no ha acabado el juego, no hay ganador
        if not self.terminal():
            return 0
        
        count_1 = 0
        count_2 = 0

        for row in range(self.rows):
            for col in range(self.cols):

                # Casillas ocupadas por el jugador 1
                if self.board[row][col] == 1:
                    count_1 += 1

                # Casillas ocupadas por el jugador 2
                elif self.board[row][col] == -1:
                    count_2 += 1

        # Determinar el ganador
        if count_1 > count_2:
            return 1    # Gana el jugador 1
        elif count_1 < count_2:
            return -1   # Gana el jugador 2
        elif count_1 == count_2:
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