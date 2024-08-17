import numpy as np
import scipy.integrate as spi

def f(x):
    return x**2

a, b = 0, 2

N = 100000

x_random = np.random.uniform(a, b, N)

y_random = f(x_random)

integral_approximation = (b - a) * np.mean(y_random)

print(f"Результат підрахкнку методом Монте-Карло: {integral_approximation}")

result, error = spi.quad(f, a, b)

print("Результат інтегрування через skipy.integrate: ", result)

print("Різниця: ", result - integral_approximation)