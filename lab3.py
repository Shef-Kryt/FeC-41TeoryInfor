import numpy as np
import matplotlib.pyplot as plt

# параметри
L = 1                 # ширина потенціальної ями
n = 1                 # квантове число

x = np.linspace(0, L, 1000)

# хвильова функція
psi = np.sqrt(2/L) * np.sin(n * np.pi * x / L)

# густина ймовірності
prob = psi**2

plt.figure()

# хвильова функція
plt.subplot(2,1,1)
plt.plot(x, psi)
plt.title("Хвильова функція ψ(x)")
plt.xlabel("x")
plt.ylabel("ψ(x)")

# густина ймовірності
plt.subplot(2,1,2)
plt.plot(x, prob)
plt.title("Густина ймовірності |ψ(x)|²")
plt.xlabel("x")
plt.ylabel("|ψ(x)|²")

plt.tight_layout()
plt.show()
for n in range(1,4):
    psi = np.sqrt(2/L) * np.sin(n*np.pi*x/L)
    plt.plot(x, psi, label=f"n={n}")

plt.title("Квантові стани частинки")
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.legend()
plt.show()