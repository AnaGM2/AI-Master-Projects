
import sys
import os
import numpy as np

sys.path.append(os.path.abspath("../methods"))
sys.path.append(os.path.abspath("../selection"))

from algorithm import Algorithm
from monte_carlo_tree_search import Node


class UCB1(Algorithm):
    def __init__(self, node: Node, c = 1):
        """
        Inicializa el algoritmo UCB1.

        :param node: Nodo actual en el árbol.
        :param c: Parámetro de ajuste que controla el grado de exploración.
        """
        super().__init__(node)
        self.c = c  # Parámetro de ajuste que controla el grado de exploración

    def set_node(self, node: Node):
        """
        Método para cambiar de nodo.
        """
        self.node = node
    
    def select_node(self) -> Node:
        """
        Selecciona el nodo hijo con el mayor valor UCB1.

        :return: El nodo hijo seleccionado.
        """
        if not self.node.children:
            raise ValueError("UCB1: no hay nodos hijos disponibles para seleccionar.")
        
        # Comprobar si hay una jugada ganadora inmediata
        for child in self.node.children:
            if child.state.terminal() and child.state.winner() == self.node.state.turn:
                return child  # Ejecutar la jugada ganadora directamente
        
        total_pulls = sum(child.N for child in self.node.children)  # Total de simulaciones realizadas
        ucb_values = np.zeros(len(self.node.children))

        for i, child in enumerate(self.node.children):
            if child.N == 0:  # Si nunca ha sido seleccionado, asignar un valor muy alto para exploración
                ucb_values[i] = float('inf')
            else:
                player_in_turn = self.node.state.turn
                Q = child.Q1 if player_in_turn == 1 else child.Q2

                # Fórmula de UCB1: Q + c * sqrt(log(total) / N)
                ucb_values[i] = Q + self.c * np.sqrt((np.log(max(total_pulls, 1))) / child.N)

        # Seleccionar el nodo con el mayor UCB1
        selected_index = np.argmax(ucb_values)
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
