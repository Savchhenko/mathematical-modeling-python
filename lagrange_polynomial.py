import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 5, -6, 7, 4, 3, 8, 9, 1, -2], dtype=float)
y = np.array([-1, 77, -297, 249, 33, 9, 389, 573, -3, -21], dtype=float)

def lagranz(x, y, t):
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
# def piecewice_linear_interpolation(x, y, xnew) = def pwlin_int()
def pwlin_int(x, y, xnew):
    for i in range(len(x) - 1):
        if x[i] <= xnew <= x[i + 1]:
            result = y[i] + (y[i + 1] - y[i]) * (xnew - x[i]) / (x[i + 1] - x[i])
            return result

fig, ax = plt.subplots()
xnew = np.linspace(np.min(x), np.max(x), 100) #массив из 100 элементов
ax.plot([lagranz(x, y, i) for i in xnew], label='lagranz')
ax.plot([pwlin_int(x, y, i) for i in xnew], label='pwlin_int')
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