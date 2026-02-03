import random

###################################
# MÉTODO: Monte-Carlo Tree Search
###################################

class Node:
    """
    Clase que representa un nodo en el árbol de búsqueda para un juego. 
    Guarda el estado del juego, su relación con otros nodos y estadísticas 
    útiles para MCTS.
    """
    def __init__(self, state, parent, action_from_parent=None):
        """
        Inicializa un nodo del árbol de búsqueda.

        Parámetros:
        state: estado actual del juego en este nodo.
        parent: nodo padre (puede ser None para la raíz).
        action_from_parent: acción que llevó desde el nodo padre a este nodo.
        """
        # Estado del juego en este nodo
        self.state = state

        # Nodo padre en el árbol
        self.parent = parent

        # Acción tomada desde el nodo padre para llegar a este nodo
        self.action_from_parent = action_from_parent

        # Lista de nodos hijos (se llenará cuando se expanda el nodo)
        self.children = []

        # Acciones que pueden tomarse en este estado (si no es terminal)
        if not self.state.terminal():
            self.remaining = state.valid_actions()
        else:
            self.remaining = []

        # Número de simulaciones que han pasado por este nodo
        self.N = 0

        # Recompensa acumulada para el jugador 1
        self.Q1 = 0

        # Recompensa acumulada para el jugador 2
        self.Q2 = 0


class MCTS:
    def __init__(self, root_node: Node, selection_algorithm_class: type, simulations: int = 1000, *selection_algorithm_args, **selection_algorithm_kwargs):
        """
        Inicializa el algoritmo Monte-Carlo Tree Search.

        :param root_node: Nodo raíz del árbol.
        :param selection_algorithm_class: Clase del algoritmo de selección.
        :param simulations: Número de simulaciones.
        :param selection_algorithm_args: Argumentos adicionales para inicializar el algoritmo de selección.
        :param selection_algorithm_kwargs: Argumentos con nombre para inicializar el algoritmo de selección.
        """
        self.root_node = root_node
        self.simulations = simulations

        # Inicializar el algoritmo de selección
        self.selection_algorithm = selection_algorithm_class(self.root_node, *selection_algorithm_args, **selection_algorithm_kwargs)

    def selection(self):
        """
        Realiza la fase de selección de MCTS: se parte del nodo raíz y se seleccionan
        nodos hijos sucesivamente hasta llegar a un nodo hoja (nodo que tiene al menos un hijo
        potencial al que no se le ha aplicado ninguna simulación todavía).

        :return: El nodo hoja encontrado.
        """
        # Partir del nodo raíz
        current_node = self.root_node

        # Repetir mientras el nodo actual no sea un nodo hoja
        while current_node.children and not current_node.remaining:

            # Actualizar el nodo en el algoritmo de selección
            self.selection_algorithm.set_node(current_node)

            # Usar el algoritmo de selección para elegir un nodo hijo
            current_node = self.selection_algorithm.select_node()

        # Devolver el nodo hoja encontrado
        return current_node
    
    def expansion(self, leaf_node):
        """
        Realiza la fase de expansión de MCTS: A partir del nodo hoja seleccionado, crear un nodo hijo 
        (movimiento válido desde el nodo hoja).

        :param leaf_node: Nodo hoja seleccionado en la fase de selección.
        :return: El nodo hijo creado.
        """
        # Si el nodo es terminal, devolverlo tal cual
        if leaf_node.state.terminal():
            return leaf_node
        
        else:
            # Tomar una acción de las restantes en el nodo
            action = leaf_node.remaining.pop()

            # Aplicar la acción sobre el estado actual para obtener el nuevo estado
            state = leaf_node.state.action(action)

            # Crear un nodo hijo a partir de dicha acción
            child_node = Node(state, parent = leaf_node, action_from_parent=action)

            # Añadir el nodo hijo a la lista de hijos
            leaf_node.children.append(child_node)

            # Devolver el nodo hijo
            return child_node

    def simulation(self, child_node):
        """
        Realiza la fase de simulación de MCTS: Completar una jugada aleatoria desde el nodo hijo creado.

        :param child_node: Nodo hijo creado en la fase de expansión.
        :return: El ganador del juego.
        """
        # Estado inicial
        state = child_node.state

        # Realizar la simulación hasta alcanzar un estado terminal
        while not state.terminal():
            # Seleccionar una acción aleatoria de entre las acciones válidas para el estado actual
            random_index = random.randint(0, len(state.valid_actions()) - 1)    # Índice aleatorio
            action = state.valid_actions()[random_index]    # Acción seleccionada aleatoriamente

            # Aplicar la acción seleccionada al estado para obtener un nuevo estado
            state = state.action(action)
 
        # Devolver el resultado del juego
        return state.winner()   # Devuelve el ganador: 1 para el jugador 1, -1 para el jugador 2

    def backpropagation(self, child_node, winner):
        """
        Realiza la fase de retropropagación de MCTS: Usar los resultados de la simulación para actualizar
        información en los nodos, recorriéndolos desde el nodo expandido hasta el nodo raíz.

        :param child_node: Nodo hijo creado en la fase de expansión.
        :param winner: Ganador del juego en la simulación.
        """
        # Se comienza en el nodo expandido
        current_node = child_node

        # Se recorren los nodos desde el nodo expandido hasta el nodo raíz
        while current_node.parent is not None:
            self.selection_algorithm.set_node(current_node.parent)
        
            # Recompensa: +1 si ganó ese jugador, -1 si perdió
            player_that_moved = -current_node.state.turn  # Jugador que hizo el movimiento para llegar a este estado
            reward = 1 if winner == player_that_moved else -1

            # Actualizar la recompensa y las visitas del jugador que movía en ese nodo
            self.selection_algorithm.update(current_node, reward)

            # Subir al nodo padre
            current_node = current_node.parent

    def run(self):
        """
        Ejecuta MCTS por el número de simulaciones especificado.
        """
        for _ in range(self.simulations):
            leaf_node = self.selection()               # Selección
            child_node = self.expansion(leaf_node)     # Expansión
            winner = self.simulation(child_node)       # Simulación
            self.backpropagation(child_node, winner)   # Retropropagación


def MCTSPlay(game_state, num_simulations, selection_algorithm_class, *selection_algorithm_args, **selection_algorithm_kwargs):
    """
    Algoritmo de Monte-Carlo Tree Search para elegir el mejor movimiento en un estado.

    Parámetros:
    - game_state: Estado actual del juego.
    - num_simulations: Número de simulaciones.
    - selection_algorithm_class: Clase del algoritmo de selección.
    - selection_algorithm_args: Argumentos adicionales para inicializar el algoritmo de selección.
    - selection_algorithm_kwargs: Argumentos con nombre para inicializar el algoritmo de selección.
    """
    # Elegir directamente la jugada ganadora si está disponible
    for action in game_state.valid_actions():
        next_state = game_state.action(action)
        if next_state.terminal() and next_state.winner() == game_state.turn:
            return next_state
        
    # Crear el nodo raíz a partir del estado actual del juego
    root_node = Node(game_state, parent=None)

    # Inicializar una clase MCTS
    mcts = MCTS(root_node, selection_algorithm_class, num_simulations, *selection_algorithm_args, **selection_algorithm_kwargs)

    # Ejecutar el algoritmo MCTS
    mcts.run()

    # Si no hay jugada ganadora inmediata, elegir la correspondiente al hijo más visitado
    best_child = max(root_node.children, key=lambda c: c.N)
    return best_child.state


class MCTSAgent:
    """
    Agente que elige jugadas usando MCTS.
    """
    def __init__(self, sims, selection_class, *selection_args, **selection_kwargs):
        self.sims = sims
        self.selection_class = selection_class
        self.selection_args = selection_args
        self.selection_kwargs = selection_kwargs
        
    def move(self, game):
        return MCTSPlay(game, self.sims, self.selection_class, *self.selection_args, **self.selection_kwargs)