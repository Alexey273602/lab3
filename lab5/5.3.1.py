import numpy as np
import math
import matplotlib.pyplot as plt

t = np.arange(2, 3.0001, 0.05)
s = np.log(1.3 + t) - np.exp(t)

print(f"Максимальное значение {np.max(s)}")
print(f"Минимальное значение {np.min(s)}")
print(f"Среднее значение {np.mean(s)}")
print(f"Количество элементов {len(s)}")
print(f"Значения отсортированные по убыванию {np.sort(s)[::-1]}")

plt.figure(figsize=(10, 5))
plt.plot(t, s, label='t', marker='o')
plt.xlabel('t')
plt.ylabel('s')
plt.grid(1)
plt.plot(t, np.full_like(t, np.mean(s)), '--', label='Cреднее значение', marker='x')
plt.legend()
plt.show()
