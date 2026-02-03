
import sys
import os
import numpy as np

sys.path.append(os.path.abspath("../methods"))
sys.path.append(os.path.abspath("../selection"))

from algorithm import Algorithm
from monte_carlo_tree_search import Node


class Softmax(Algorithm):
    def __init__(self, node: Node, tau = 1):
        """
        Inicializa el algoritmo Softmax.

        :param node: Nodo actual en el árbol de búsqueda.
        :param tau: Parámetro que controla el equilibrio entre exploración y explotación.
        :raises ValueError: Si tau no es mayor que 0.
        """
        assert tau > 0, "El parámetro tau debe ser mayor que 0."

        super().__init__(node)
        self.tau = tau

    def set_node(self, node: Node):
        """
        Método para cambiar de nodo.
        """
        self.node = node

    def select_node(self) -> Node:
        """
        Selecciona un nodo hijo basado en la política Softmax.
        :return: El nodo hijo seleccionado.
        """
        if not self.node.children:
            raise ValueError("Softmax: no hay nodos hijos disponibles para seleccionar.")
        
        # Comprobar si hay una jugada ganadora inmediata
        for child in self.node.children:
            if child.state.terminal() and child.state.winner() == self.node.state.turn:
                return child  # Ejecutar la jugada ganadora directamente

        # Calcular las probabilidades de selección para cada nodo hijo
        player_in_turn = self.node.state.turn
        Q_values = [child.Q1 if player_in_turn == 1 else child.Q2 for child in self.node.children]
        Q_values = np.array(Q_values)
        Q_stable = Q_values - np.max(Q_values)  # Estabilizar los valores
        exp_values = np.exp(Q_stable / self.tau)
        prob = exp_values / np.sum(exp_values)

        # Seleccionar un nodo hijo de acuerdo con la distribución de probabilidad calculada
        selected_index = np.random.choice(len(self.node.children), p=prob)

        return self.node.children[selected_index]

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

