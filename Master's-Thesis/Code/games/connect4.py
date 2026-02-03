
###############################
# JUEGO: 4 en raya
###############################

# 4 en raya es un juego de estrategia para dos jugadores que consiste en alinear cuatro fichas del mismo color en un tablero vertical.

# Reglas:
# - El juego clásico se juega en un tablero de 7 columnas por 6 filas (aunque en esta implementación pueden tomar valores entre 4 y 10)
# - Los jugadores se turnan para dejar caer una ficha en una de las columnas
# - La ficha cae hasta ocupar la posición más baja disponible en esa columna
# - El objetivo es alinear cuatro fichas consecutivas del mismo color (en línea horizontal, vertical o diagonal)
# - Gana el primer jugador que consiga alinear cuatro fichas

class Connect4Game:
    def __init__(self, rows=6, cols=7, starting_player=1):
        """
        Inicializa el juego

        Parámetros:
        - rows: El número de filas del tablero del juego (por defecto 6, puede tomar valores entre 4 y 10)
        - cols: El número de columnas del tablero del juego (por defecto 7, puede tomar valores entre 4 y 10)
        - starting_player: El jugador que inicia el juego, 1 o -1 (por defecto 1)
        """
        assert 4 <= rows <= 10, "El número de filas debe estar entre 4 y 10."
        assert 4 <= cols <= 10, "El número de columnas debe estar entre 4 y 10."
        assert starting_player in (1, -1), "El jugador inicial debe ser 1 o -1."

        self.rows = rows
        self.cols = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]  # Definir el tablero
        self.turn = starting_player
        self.eval = []  # Evaluaciones de las simulaciones

    def valid_actions(self):
        """
        Devuelve una lista con las columnas válidas donde se puede colocar una ficha
        """
        valid_moves = []

        for col in range(self.cols):    # Iterar por cada columna
            # Encontrar la primera fila vacía en esa columna
            for row in range(self.rows-1, -1, -1):  # Iterar por cada fila de abajo hacia arriba
                if self.board[row][col] == 0:   # Celda vacía
                    valid_moves.append(col)
                    break   # No hace falta seguir buscando, ya se ha encontrado una fila vacía en esa columna
        return valid_moves
    
    def action(self, col):
        """
        Realiza un turno del juego
        """
        # Verificar si la columna es válida
        if col not in self.valid_actions():
            raise ValueError(f"Acción inválida: la columna {col + 1} está llena. Por favor, elige una columna con espacio disponible.")
        
        # Crear una copia del tablero actual para el nuevo juego
        new_board = [row[:] for row in self.board]

        # Colocar la ficha en la primera fila vacía de la columna seleccionada
        for row in range(self.rows-1, -1, -1):  # Iterar por cada fila de abajo hacia arriba
            # Encontrar la primera celda vacía desde abajo y colocar la ficha
            if new_board[row][col] == 0:
                new_board[row][col] = self.turn
                break

        # Crear un nuevo juego con el tablero actualizado
        new_game = Connect4Game(self.rows, self.cols, -self.turn)
        new_game.board = new_board    # Asignar el nuevo tablero
        new_game.eval = self.eval[:]  # Copiar el historial de evaluaciones
        return new_game

    def terminal(self):
        """
        Devuelve True si el juego ha terminado (cuando un jugador alinee 4 fichas consecutivas)
        """
        # Si hay un ganador
        if self.winner() != 0:
            return True
        
        # Si el tablero está lleno (empate)
        if all(self.board[0][col] != 0 for col in range(self.cols)):
            return True

        # Si el juego no ha terminado
        return False

    def winner(self):
        """
        Devuelve el ganador: 1 para el jugador 1, -1 para el jugador 2
        """
        # Comprobar si hay 4 fichas consecutivas del mismo jugador
        for row in range(self.rows):
            for col in range(self.cols):

                # Comprobar si la celda actual contiene una ficha
                if self.board[row][col] in (1, -1):

                    # Obtener el jugador de la ficha en la celda actual
                    player = self.board[row][col]

                    # En horizontal
                    if col + 4 <= self.cols:    # Verificar si hay espacio suficiente a la derecha
                        if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                            return player

                    # En vertical
                    if row + 4 <= self.rows:    # Verificar si hay espacio suficiente abajo
                        if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                            return player
                        
                    # En diagonal descendente
                    if row + 4 <= self.rows and col + 4 <= self.cols:   # Verificar si hay espacio suficiente en la diagonal
                        if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
                            return player

                    # En diagonal ascendente
                    if row > 3 and col + 4 <= self.cols:    # Verificar si hay espacio suficiente en la diagonal
                        if self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3]:
                            return player

        # Si no se encuentran 4 fichas consecutivas del mismo jugador
        return 0

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
