import numpy as np
from src.functions import fitness

def run_ga(
        pop_size: int = 50,
        n_generations: int = 50,
        mutation_sigma: float = 0.05,
        seed: int = 0
):
    """
    Ejecuta un algoritmo genético mínimo para maximizar la función fitness.
        
    :param pop_size: Número de individuos en la población.
    :type pop_size: int
    :param n_generations: Número de generaciones a simular.
    :type n_generations: int
    :param mutation_sigma: Desviación estándar de la mutación gaussiana.
    :type mutation_sigma: float
    :param seed: Semilla para reproducibilidad.
    :type seed: int
    """

    # Generador de números aleatorios (reproducible)
    rng = np.random.default_rng(seed)
    
    # --------------------------------------------------
    # 1. Inicializar población
    # --------------------------------------------------

    # Cada individuo es un número real en el rango [0, 1]
    population = rng.uniform(
        low=0.0,
        high=1.0,
        size=pop_size
    )

    # Guardamos el mejor individuo encontrado
    best_x = None
    best_fitness = -np.inf

    # --------------------------------------------------
    # Bucle evolutivo principal
    # --------------------------------------------------

    for generation in range(n_generations):

        # 2. Evaluar fitness de la población actual
        fitness_values = fitness(population)

        # Actualizar el mejor individuo global
        gen_best_idx = np.argmax(fitness_values)
        gen_best_fitness = fitness_values[gen_best_idx]
        gen_best_x = population[gen_best_idx]

        if gen_best_fitness > best_fitness:
            best_fitness = gen_best_fitness
            best_x = gen_best_x

        # 3. Selección de padres (torneo tamaño 2)
        parents = []
        for _ in range(pop_size):
            i, j = rng.integers(0, pop_size, size=2)

            if fitness_values[i] > fitness_values[j]:
                parents.append(population[i])
            else:
                parents.append(population[j])

        parents = np.array(parents)

        # 4. Mutación (crear descendencia)
        offspring = parents + rng.normal(
            loc=0.0,
            scale=mutation_sigma,
            size=pop_size
        )

        # Mantener los individuos en el rango válido
        offspring = np.clip(offspring, 0.0, 1.0)

        # 5. Reemplazo generacional
        population = offspring

    # --------------------------------------------------
    # Resultado final
    # --------------------------------------------------
    return best_x, best_fitness