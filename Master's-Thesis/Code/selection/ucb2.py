
import sys
import os
import numpy as np

sys.path.append(os.path.abspath("../methods"))
sys.path.append(os.path.abspath("../selection"))

from algorithm import Algorithm
from monte_carlo_tree_search import Node


class UCB2(Algorithm):
    def __init__(self, node: Node, alpha: float = 0.5):
        """
        Inicializa el algoritmo UCB2.

        :param node: Nodo actual en el árbol.
        :param alpha: Parámetro para regular la exploración. Valores más grandes aumentan la exploración.
        :raises ValueError: Si alpha no está en (0, 1).
        """
        assert 0 < alpha < 1, "El parámetro alpha debe estar entre 0 y 1."

        super().__init__(node)
        self.alpha = alpha  # Parámetro que regula la exploración
        self.d_ka = {}      # Número de épocas para cada nodo
        self.d_remaining_plays = {} # Jugadas restantes por nodo

    def set_node(self, node: Node):
        """
        Método para cambiar de nodo.
        """
        self.node = node
        self.d_ka = {}
        self.d_remaining_plays = {}
    
    def select_node(self) -> Node:
        """
        Selecciona el nodo hijo con el mayor valor UCB2.

        :return: El nodo hijo seleccionado.
        """
        if not self.node.children:
            raise ValueError("UCB2: no hay nodos hijos disponibles para seleccionar.")
        
        # Comprobar si hay una jugada ganadora inmediata
        for child in self.node.children:
            if child.state.terminal() and child.state.winner() == self.node.state.turn:
                return child  # Ejecutar la jugada ganadora directamente
            
        # Inicializar los nuevos hijos en los diccionarios
        for child in self.node.children:
            if child not in self.d_ka:
                self.d_ka[child] = 0
                self.d_remaining_plays[child] = 0

        # Revisar si algún hijo está en medio de una época
        for child in self.node.children:
            if self.d_remaining_plays[child] > 0:
                self.d_remaining_plays[child] -= 1
                return child
            
        total_pulls = sum(child.N for child in self.node.children)  # Total de simulaciones realizadas
        ucb_values = np.zeros(len(self.node.children))

        for i, child in enumerate(self.node.children):
            if child.N == 0:  # Si nunca ha sido seleccionado, asignar un valor muy alto para exploración
                ucb_values[i] = float('inf')
            else:
                player_in_turn = self.node.state.turn
                Q = child.Q1 if player_in_turn == 1 else child.Q2

                # Fórmula de UCB2: Q + sqrt(((1 + alpha) * log(e*total/tau_ka)) / (2 * tau_ka))
                ka = self.d_ka[child]
                tau_ka = np.ceil((1 + self.alpha) ** ka)
                ratio = np.exp(1) * total_pulls / max(tau_ka, 1)
                log_term = np.log(ratio) if ratio > 0 else 0
                sqrt_term = np.sqrt(((1 + self.alpha) * log_term) / (2 * tau_ka)) if log_term > 0 else 0
                ucb_values[i] = Q + sqrt_term

        # Seleccionar el nodo con el mayor UCB2
        selected_index = np.argmax(ucb_values)
        selected_node = self.node.children[selected_index]

        # Nueva época
        ka = self.d_ka[selected_node]
        tau_ka = np.ceil((1 + self.alpha) ** ka)
        tau_ka_plus_1 = np.ceil((1 + self.alpha) ** (ka + 1))
        
        # Número de veces que el nodo será seleccionado en la nueva época
        time_block = int(tau_ka_plus_1 - tau_ka)    

        self.d_remaining_plays[selected_node] = time_block - 1
        self.d_ka[selected_node] += 1

        return selected_node
    
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