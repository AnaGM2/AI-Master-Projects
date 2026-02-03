
import sys
import os
import numpy as np

sys.path.append(os.path.abspath("../methods"))
sys.path.append(os.path.abspath("../selection"))

from algorithm import Algorithm
from monte_carlo_tree_search import Node


class AdaptiveSoftmax(Algorithm):
    def __init__(self, node: Node, tau_0 = 1, alpha = 0.5):
        """
        Inicializa el algoritmo AdaptiveSoftmax con ajuste dinámico de tau.

        :param node: Nodo actual en el árbol de búsqueda.
        :param tau_0: Valor inicial del parámetro tau.
        :param alpha: Parámetro de ajuste para la disminución de tau (0.001 - 1 | Exploración - Explotación).
        """
        assert tau_0 > 0, "El parámetro tau_0 debe ser mayor que 0."
        assert 0 < alpha <= 1, "El parámetro alpha debe estar entre 0 y 1."

        super().__init__(node)
        self.tau_0 = tau_0
        self.alpha = alpha
        self.t = 0  # Contador de iteraciones

    def set_node(self, node: Node):
        """
        Método para cambiar de nodo.
        """
        self.node = node
        self.t = 0

    def select_node(self) -> Node:
        """
        Selecciona un nodo hijo basado en la política Softmax con tau adaptativo.
        :return: Nodo hijo seleccionado.
        """
        if not self.node.children:
            raise ValueError("AdaptiveSoftmax: no hay nodos hijos disponibles para seleccionar.")
        
        # Comprobar si hay una jugada ganadora inmediata
        for child in self.node.children:
            if child.state.terminal() and child.state.winner() == self.node.state.turn:
                return child  # Ejecutar la jugada ganadora directamente
        
        # Ajuste dinámico de tau
        tau = max(self.tau_0 / (1 + self.alpha * self.t), 1e-2)  # Evitar tau demasiado pequeño

        # Obtener valores Q de los nodos hijos
        player_in_turn = self.node.state.turn
        Q_values = [child.Q1 if player_in_turn == 1 else child.Q2 for child in self.node.children]
        Q_values = np.array(Q_values)
        Q_stable = Q_values - np.max(Q_values)  # Estabilizar los valores
        exp_values = np.exp(np.clip(Q_stable / tau, -500, 500))  # Evita desbordamientos
        prob = exp_values / np.sum(exp_values)  # Normalización de Softmax
    
        # Seleccionar nodo de acuerdo con la distribución de probabilidad
        selected_index = np.random.choice(len(self.node.children), p=prob)
        
        return self.node.children[selected_index]

    def update(self, chosen_node: Node, reward: float):
        """
        Actualiza la recompensa y las visitas para el nodo hijo seleccionado, y el contador de iteraciones.

        :param chosen_node: El nodo hijo seleccionado.
        :param reward: La recompensa obtenida para ese nodo.
        """
        self.t += 1     # Actualizar contador
        
        chosen_node.N += 1  # Incrementar el número de visitas del nodo hijo

        # Actualizar recompensa promedio
        player_that_moved = -chosen_node.state.turn
        if player_that_moved == 1:
            chosen_node.Q1 += (reward - chosen_node.Q1) / chosen_node.N
        elif player_that_moved == -1:
            chosen_node.Q2 += (reward - chosen_node.Q2) / chosen_node.N
        
