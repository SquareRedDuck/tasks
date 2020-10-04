from pathlib import Path as pth
from matplotlib import pyplot as plt
import numpy as np

A = 9.66459
x = np.linspace(-10, 10, 10)

def f(x):
    return -abs(np.sin(x) * np.cos(A) * np.exp(abs(1 - (np.sqrt(x ** 2 + A ** 2) / np.pi))))
y = f(x)
print(y)
p = pth('results')
res = p / 'task_01_307b_Gusev_8.txt'
if not p.exists():
    p.mkdir(exist_ok=True)
    
if p.exists():
    with res.open('w') as f:
        i = 0
        for _x in x:
            f.write(str(_x) + ' ' + str(y[i]) + '\n')
            i += 1
else:
    print("Error: \'results\' dir does not exists")

plt.plot(x, y)
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
