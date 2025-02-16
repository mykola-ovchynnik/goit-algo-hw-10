import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 1.856  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()


N = 10000
x_rand = np.random.uniform(a, b, N)
f_values = f(x_rand)
mc_integral = (b - a) * np.mean(f_values)


analytic_integral = (b**3) / 3 - (a**3) / 3


result, error = spi.quad(f, a, b)


print(f"Оцінка інтеграла методом Монте-Карло: {mc_integral}")
print(f"Аналітичне значення інтеграла : {analytic_integral}")
print("Інтеграл: ", result, error)
