
import sys
import os
import numpy as np

sys.path.append(os.path.abspath("../methods"))
sys.path.append(os.path.abspath("../selection"))

from algorithm import Algorithm
from monte_carlo_tree_search import Node


class GradienteDePreferencias(Algorithm):
    def __init__(self, node: Node, alpha: float = 0.2):
        """
        Inicializa el algoritmo de Gradiente de Preferencias.

        :param node: Nodo actual en el árbol de búsqueda.
        :param alpha: Tasa de aprendizaje para actualizar las preferencias.
        """
        super().__init__(node)
        self.alpha = alpha  # Tasa de aprendizaje
        self.preferences = []  # Preferencias iniciales de los nodos
        self.action_probabilities = []  # Probabilidades iniciales
        self.average_reward = 0  # Promedio de las recompensas recibidas
        self.time_step = 0  # Contador de iteraciones

    def set_node(self, node: Node):
        """
        Método para cambiar de nodo.
        """
        self.node = node
        self.preferences = np.zeros(len(self.node.children))
        self.action_probabilities = np.ones(len(self.node.children)) / len(self.node.children)  # Probabilidades iniciales uniformes
        self.average_reward = 0  # Promedio de las recompensas recibidas
        self.time_step = 0  # Contador de iteraciones

    def select_node(self) -> Node:
        """
        Selecciona un nodo hijo basado en la distribución de probabilidad Softmax sobre las preferencias.
        
        :return: El nodo hijo seleccionado.
        """
        if not self.node.children:
            raise ValueError("GradienteDePreferencias: no hay nodos hijos disponibles para seleccionar.")
        
        # Comprobar si hay una jugada ganadora inmediata
        for child in self.node.children:
            if child.state.terminal() and child.state.winner() == self.node.state.turn:
                return child  # Ejecutar la jugada ganadora directamente
            
        exp_preferences = np.exp(self.preferences - np.max(self.preferences))   # Evita desfases numéricos
        self.action_probabilities = exp_preferences / np.sum(exp_preferences)   # Softmax sobre las preferencias

        # Seleccionar un nodo hijo según la distribución de probabilidad
        selected_index = np.random.choice(len(self.node.children), p=self.action_probabilities)

        return self.node.children[selected_index]

    def update(self, chosen_node: Node, reward: float):
        """
        Actualiza las preferencias del algoritmo basándose en la recompensa obtenida.

        :param chosen_node: El nodo hijo seleccionado.
        :param reward: Recompensa recibida.
        """
        # Incrementar el número de visitas del nodo hijo
        chosen_node.N += 1 

        # Actualizar recompensa promedio
        player_that_moved = -chosen_node.state.turn
        if player_that_moved == 1:
            chosen_node.Q1 += (reward - chosen_node.Q1) / chosen_node.N
        elif player_that_moved == -1:
            chosen_node.Q2 += (reward - chosen_node.Q2) / chosen_node.N

        # Actualización del Gradiente de Preferencias
        self.time_step += 1
        self.average_reward += (reward - self.average_reward) / self.time_step  # Actualización incremental de la recompensa promedio

        baseline = self.average_reward
        chosen_index = self.node.children.index(chosen_node)  # Índice del nodo hijo seleccionado
        
        # Actualizar preferencias de cada nodo hijo según el gradiente de preferencias
        for i in range(len(self.node.children)):
            if i == chosen_index:
                self.preferences[i] += self.alpha * (reward-baseline) * (1 - self.action_probabilities[i])
            else:
                self.preferences[i] -= self.alpha * (reward-baseline) * self.action_probabilities[i]
