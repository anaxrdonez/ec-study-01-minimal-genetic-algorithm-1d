import numpy as np
import matplotlib.pyplot as plt
from src.functions import fitness
from src.ga import run_ga

xs = np.linspace(0.0, 1.0, 1000)
ys = fitness(xs)

best_x, best_fit = run_ga(
    pop_size= 50,
    n_generations= 80,
    mutation_sigma= 0.05,
    seed= 0
)

print(f"Best x found: {best_x:.6f}")
print(f"Best fitness: {best_fit:.3f}")


plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("fitness")
plt.title("Fitness landscape")
best_y = fitness(np.array([best_x]))[0]
plt.scatter([best_x], [best_y])
plt.annotate(
    f"best x = {best_x:.3f}\nfitness = {best_fit:3f}",
    (best_x,best_y),
    textcoords= "offset points",
    xytext=(10,10)
)

plt.show()

