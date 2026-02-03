
###############################
# JUEGO: Nim
###############################

# Nim es un juego estratégico en el que dos jugadores se turnan para retirar palos de un montón.

# Reglas:
# - Se comienza con un número determinado de palos
# - En cada turno, el jugador puede retirar entre 1 y un máximo de palos permitido
# - Los jugadores alternan turnos hasta que no queden palos
# - Gana quien tome el último palo

class NimGame:
    def __init__(self, initial_sticks=21, max_sticks_per_turn=4, starting_player=1):
        """
        Inicializa el juego

        Parámetros:
        - initial_sticks: El número de palos al inicio del juego (por defecto 21)
        - max_sticks_per_turn: El número máximo de palos que se pueden retirar en un turno (por defecto 4)
        - starting_player: El jugador que inicia el juego, 1 o -1 (por defecto 1)
        """
        assert starting_player in (1, -1), "El jugador inicial debe ser 1 o -1."
        
        self.sticks = initial_sticks
        self.max_sticks_per_turn = max_sticks_per_turn
        self.turn = starting_player
        self.eval = []  # Evaluaciones de las simulaciones

    def valid_actions(self):
        """
        Devuelve una lista con las acciones válidas
        """
        return [i for i in range(1, min(self.max_sticks_per_turn, self.sticks) + 1)] if self.sticks > 0 else []
    
    def action(self, amount):
        """
        Realiza un turno del juego, restando el número especificado de palos
        """
        if amount not in self.valid_actions():
            raise ValueError(f"Acción inválida: solo puedes retirar entre 1 y {self.max_sticks_per_turn} palos, "
                             "y no más de los que quedan.")
        
        # Devolver un nuevo estado del juego con los valores actualizados
        new_game = NimGame(self.sticks - amount, self.max_sticks_per_turn, -self.turn)
        new_game.eval = self.eval[:]  # Copiar el historial de evaluaciones
        return new_game

    def terminal(self):
        """
        Devuelve True si el juego ha terminado (cuando no quedan palos)
        """
        return self.sticks == 0

    def winner(self):
        """
        Devuelve el ganador: 1 para el jugador 1, -1 para el jugador 2
        """
        return -self.turn if self.terminal() else 0

    def draw(self):
        """
        Dibuja el estado actual del juego
        """
        if self.sticks == 1:
            print(f"Queda {self.sticks} palo.")
        else:
            print(f"Quedan {self.sticks} palos.")