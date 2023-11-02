import numpy as np
import matplotlib.pyplot as plt
import random

#Usei o random.unifome porque ele vai limitar os pontos entre o intervalo -10 e 10 para as coordenadas 
P_0 = [random.uniform(-10, 10), random.uniform(-10, 10)]
P_1 = [random.uniform(-10, 10), random.uniform(-10, 10)]
P_2 = [random.uniform(-10, 10), random.uniform(-10, 10)]
P_3 = [random.uniform(-10, 10), random.uniform(-10, 10)]

N = 100
P = np.zeros((N, 2))

triPascal = [[1, 3, 3, 1], [1, 2, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0]]

for k in range(N):
    t = k / (N - 1)
    mt = 1 - t
    mt2 = mt * mt
    mt3 = mt2 * mt
    t2 = t * t
    t3 = t2 * t
    x = mt3 * P_0[0] * triPascal[0][0] + 3 * mt2 * t * P_1[0] * triPascal[0][1] + 3 * mt * t2 * P_2[0] * triPascal[0][2] + t3 * P_3[0] * triPascal[0][3]
    y = mt3 * P_0[1] * triPascal[0][0] + 3 * mt2 * t * P_1[1] * triPascal[0][1] + 3 * mt * t2 * P_2[1] * triPascal[0][2] + t3 * P_3[1] * triPascal[0][3]
    P[k] = [x, y]

plt.scatter([P_0[0], P_1[0], P_2[0], P_3[0]], [P_0[1], P_1[1], P_2[1], P_3[1],], color='red', label='Pontos de Controle')

plt.plot([P_0[0], P_1[0]], [P_0[1], P_1[1]], color='blue')
plt.plot([P_1[0], P_2[0]], [P_1[1], P_2[1]], color='blue')
plt.plot([P_2[0], P_3[0]], [P_2[1], P_3[1]], color='blue')


plt.plot(P[:,0], P[:,1], color='green', label='Curva de Bézier')

plt.legend()
plt.grid()
plt.show()
