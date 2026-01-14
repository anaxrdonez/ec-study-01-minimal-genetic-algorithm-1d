import numpy as np

def fitness(x: np.ndarray) -> np.ndarray:
    """
    Función objetivo a maximizar.
    x debe estar entre el rango [0,1]
    """
    fitness_= x* np.sin(10 * x) + 1.0
    return fitness_