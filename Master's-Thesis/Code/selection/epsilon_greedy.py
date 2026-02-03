
import sys
import os
import numpy as np

sys.path.append(os.path.abspath("../methods"))
sys.path.append(os.path.abspath("../selection"))

from algorithm import Algorithm
from monte_carlo_tree_search import Node


class EpsilonGreedy(Algorithm):
    def __init__(self, node: Node, epsilon: float = 0.1):
        """
        Inicializa el algoritmo epsilon-greedy.

        :param node: Nodo actual en el árbol de búsqueda.
        :param epsilon: Probabilidad de exploración (seleccionar un nodo al azar).
        :raises ValueError: Si epsilon no está en [0, 1].
        """
        assert 0 <= epsilon <= 1, "El parámetro epsilon debe estar entre 0 y 1."

        super().__init__(node)
        self.epsilon = epsilon
        self.node_exploration_map = {}

        self.ensure_node_initialized(self.node)

    def ensure_node_initialized(self, node: Node):
        """
        Asegura que el nodo tenga un conjunto de hijos por explorar registrado.
        """
        node_id = id(node)
        if node_id not in self.node_exploration_map:
            self.node_exploration_map[node_id] = list(range(len(node.children)))

    def set_node(self, node: Node):
        """
        Método para cambiar de nodo y reiniciar el conjunto de exploración.
        """
        self.node = node
        self.ensure_node_initialized(node)

    def select_node(self) -> Node:
        """
        Selecciona un nodo hijo basado en la política epsilon-greedy, asegurando que cada nodo hijo
        sea seleccionado al menos una vez antes de iniciar la exploración/explotación normal.

        :return: El nodo hijo seleccionado.
        """
        if not self.node.children:
            raise ValueError("EpsilonGreedy: no hay nodos hijos disponibles para seleccionar.")
        
        # Comprobar si hay una jugada ganadora inmediata
        for child in self.node.children:
            if child.state.terminal() and child.state.winner() == self.node.state.turn:
                return child  # Ejecutar la jugada ganadora directamente
        
        # Inicialización: asegurar que cada hijo se explore al menos una vez
        node_id = id(self.node)
        unexplored = self.node_exploration_map[node_id]
        if unexplored:
            # Extraer y eliminar un nodo hijo del conjunto de nodos no explorados
            index = unexplored.pop()
            return self.node.children[index]
            
        # Exploración: seleccionar un nodo hijo aleatorio
        if np.random.random() < self.epsilon:
            # Selecciona un brazo al azar
            return np.random.choice(self.node.children)
        
        # Explotación: seleccionar el nodo hijo con el valor Q más alto
        else:
            # Selecciona el brazo con la mayor recompensa acumulada Q
            player_in_turn = self.node.state.turn
            Q_values = [child.Q1 if player_in_turn == 1 else child.Q2 for child in self.node.children]
            return self.node.children[np.argmax(Q_values)]

    def update(self, chosen_node: Node, reward: float):
        """
        Actualiza las recompensas y visitas para el nodo hijo seleccionado.

        :param chosen_node: El nodo hijo seleccionado.
        :param reward: La recompensa obtenida para ese nodo.
        """
        chosen_node.N += 1  # Incrementar el número de visitas del nodo hijo

        # Actualizar recompensa promedio
        player_that_moved = -chosen_node.state.turn
        if player_that_moved == 1:
            chosen_node.Q1 += (reward - chosen_node.Q1) / chosen_node.N
        elif player_that_moved == -1:
            chosen_node.Q2 += (reward - chosen_node.Q2) / chosen_node.N