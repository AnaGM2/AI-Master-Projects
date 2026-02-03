
import sys
import os
from abc import ABC, abstractmethod

sys.path.append(os.path.abspath("../methods"))

from monte_carlo_tree_search import Node


class Algorithm(ABC):
    def __init__(self, node: Node):
        """
        Inicializa el algoritmo con un nodo.

        :param node: Nodo actual.
        """
        # Nodo actual
        self.node = node

        # Número de nodos hijos = hijos ya expandidos + acciones aún no exploradas
        self.k = len(node.remaining) + len(node.children)

    def set_node(self, node: Node):
        """
        Cambia de nodo.

        :param node: Nuevo nodo.
        """
        self.node = node

    @abstractmethod
    def select_node(self) -> Node:
        """
        Selecciona un nodo hijo basado en la política de selección.

        :return: El nodo hijo seleccionado (acción a tomar).
        """
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

    def update(self, chosen_node: Node, reward: float):
        """
        Actualiza las recompensas y visitas para el nodo hijo seleccionado.

        :param chosen_node: El nodo hijo seleccionado.
        :param reward: La recompensa obtenida para ese nodo.
        """
        chosen_node.N += 1  # Incrementar el número de visitas del nodo hijo

        # Actualización incremental de la recompensa promedio
        # value = value + (reward - value) / n

        chosen_node.Q += (reward - chosen_node.Q) / chosen_node.N  # Actualizar recompensa promedio
    
    def reset(self):
        """
        Reinicia el estado del algoritmo.
        """
        for child in self.node.children:
            child.N = 0
            child.Q = 0
