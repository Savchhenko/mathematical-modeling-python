import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 5, -6, 7, 4, 3, 8, 9, 1, -2], dtype=float)
y = np.array([-1, 77, -297, 249, 33, 9, 389, 573, -3, -21], dtype=float)

# polinomial lagrange function:
def lagrange(x, y, t):
    # z = []
    z = 0
    for j in range(len(y)):
        # polynomial = 0
        #промежуточные значения полинома
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        #находим полином
        z += y[j] * p1 / p2
        # z.append(polynomial)
    return z

# piecewise linear interpolation function:
def pw_lin_int(x, y, xnew):
    for i in range(len(x) - 1):
        if x[i] <= xnew <= x[i + 1]:
            result = y[i] + (y[i + 1] - y[i]) * (xnew - x[i]) / (x[i + 1] - x[i])
            return result

# piecewise parabolic interpolation function:
def pw_parab_int(x, y, xnew):
    for i in range(len(x)):
        y0 = y[i - 1]
        y1 = y[i]
        y2 = y[i + 1]
        x0 = x[i - 1]
        x1 = x[i]
        x2 = x[i + 1]
        result = y0 + (y1 - y0)*(xnew - x0)/(x1 - x0) + (1/(x2 - x0))*(xnew - x0)*(xnew - x1)*(((y2 - y1)/(x2 - x1)) - ((y1 - y0)/(x1 - x0)))
        return result

fig, ax = plt.subplots()

xnew = np.linspace(np.min(x), np.max(x), 100) #массив
ax.plot([lagrange(x, y, i) for i in xnew], marker = 'o', markersize = 1, label='lagrange')
ax.plot([pw_lin_int(x, y, i) for i in xnew], label='pw_lin_int')
ax.plot([pw_parab_int(x, y, i) for i in xnew], label='pw_parab_int')
ax.legend()
plt.grid(True) #добавление сетки на графике
plt.show()

# xnew = np.linspace(np.min(x), np.max(x), 100) #массив из 100 элементов
# ynew1 = [lagranz(x, y, i) for i in xnew]
# ynew2 = [pwlin_int(x, y, i) for i in xnew]
# plt.plot(x, y, 'o', xnew, ynew)
# plt.grid(True) #добавление сетки на графике
# plt.show()
# print(ynew)