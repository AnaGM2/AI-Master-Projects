import numpy as np

###############################
# MÉTODO: Monte-Carlo
###############################

def rollout(root, n):
    """
    Simulación de Rollout (partida completa moviendo al azar)

    Parámetros:
    - root: Estado inicial del juego
    - n: Número de simulaciones
    """
    # Contadores de partidas ganadas por cada jugador
    P = 0
    N = 0
    for _ in range(n):
        g = root
        while not g.terminal():   # El juego no ha terminado
            # Obtener las acciones válidas
            valid_actions = g.valid_actions()

            # Seleccionar un índice aleatorio
            index = np.random.choice(range(len(valid_actions)))

            # Seleccionar la acción correspondiente al índice
            action = valid_actions[index]

            # Ejecutar la acción
            g = g.action(action)

        # Comprobar qué jugador ganó el juego
        if g.winner() > 0:
            P += 1
        if g.winner() < 0:
            N += 1
    return P,N,n


def MCPlay(g, n):
    """
    Algoritmo de Monte-Carlo para elegir el mejor movimiento en un estado

    Parámetros:
    - g: Estado actual del juego
    - n: Número de simulaciones para cada posible movimiento
    """
    acts = g.valid_actions()        # Acciones posibles
    pn = 0 if g.turn == 1 else 1    # Seleccionar al jugador

    # Simular los juegos para cada acción y almacenar las probabilidades de ganar
    probs = [rollout(g.action(a), n)[pn] for a in acts]
    #print(probs)

    # Seleccionar la acción con mayor probabilidad de éxito
    selected = acts[np.argmax(np.array(probs))]
    #print(f'La computadora juega {selected}')

    # Ejecutar el movimiento seleccionado
    g = g.action(selected)

    # Evaluar el movimiento
    g.eval.append((-g.turn, max(probs)/n))
    return g


class MCAgent:
    def __init__(self, sims):
        self.sims = sims
    def move(self, game):
        return MCPlay(game, self.sims)
