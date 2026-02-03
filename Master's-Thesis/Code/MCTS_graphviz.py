
from graphviz import Digraph


def generate_tree_MCTS(root_node, max_depth=1, filename='arbol_mcts', format='pdf'):
    """
    Genera un árbol a partir de un nodo raíz de MCTS y lo guarda.

    Parámetros:
    - root_node: Nodo raíz del árbol.
    - max_depth: Profundidad máxima a recorrer.
    - filename: Nombre del archivo generado.
    - format: Formato del archivo generado.

    Devuelve:
    - Un diccionario que mapea IDs de nodo (str) a objetos nodo (Node).
    """
    # Inicializar el grafo
    dot = Digraph(comment='Árbol MCTS')

    counter = 0  # Contador de nodos
    id_to_node = {}  # Diccionario ID -> Nodo

    # Crear ID y etiqueta para el nodo raíz
    node_id = f"nodo{counter}"
    counter += 1
    label = f"ID: {node_id}\\nTurno: {root_node.state.turn}\\nVisitas: {root_node.N}\\nRecompensa 1: {root_node.Q1}\\nRecompensa 2: {root_node.Q2}"
    
    # # Añadir nodo al grafo
    dot.node(node_id, label)

    # Guardar en el diccionario y añadir al stack
    id_to_node[node_id] = root_node
    stack = [(root_node, node_id, 0)]

    # Recorrer el árbol en profundidad hasta max_depth
    while stack:
        node, node_id, depth = stack.pop()  # Extraer un nodo del stack
        if depth < max_depth:

            # Recorrer los nodos hijos
            for child_node in node.children:

                # Crear ID y etiqueta para el nodo hijo
                child_id = f"nodo{counter}"
                counter += 1
                label = (f'ID: {child_id}\\nTurno: {child_node.state.turn}\\nVisitas: {child_node.N}'
                         f'\\nRecompensa 1: {child_node.Q1}\\nRecompensa 2: {child_node.Q2}')
                edge_label = f"Acción: {child_node.action_from_parent}"   # Acción desde el nodo padre

                # Añadir nodo y arista al grafo
                dot.node(child_id, label)
                dot.edge(node_id, child_id, label=edge_label)

                # Guardar en el diccionario y añadir al stack
                id_to_node[child_id] = child_node
                stack.append((child_node, child_id, depth + 1))

    # Renderizar el grafo
    dot.render(filename, format=format, view=True)

    return id_to_node