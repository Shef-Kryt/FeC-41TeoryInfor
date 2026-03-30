import numpy as np
import matplotlib.pyplot as plt

# ---------- Параметри ----------
omega_m = 14                 # практична ширина спектра
dt = np.pi / omega_m         # крок дискретизації

# ---------- Сигнал ----------
t = np.linspace(0, 5, 1000)
f = 2 * np.exp(-t)

# ---------- Дискретні відліки ----------
t_samples = np.arange(0, 5, dt)
f_samples = 2 * np.exp(-t_samples)

# ---------- Спектр ----------
omega = np.linspace(0, 30, 1000)
F2 = 4 / (1 + omega**2)      # |F(ω)|^2

# ---------- Графіки ----------
plt.figure()

# Сигнал
plt.subplot(3,1,1)
plt.plot(t, f)
plt.title("Сигнал f(t)=2e^{-t}")
plt.xlabel("t")
plt.ylabel("f(t)")

# Спектр
plt.subplot(3,1,2)
plt.plot(omega, F2)
plt.axvline(omega_m, linestyle='--')
plt.title("Спектр |F(ω)|^2")
plt.xlabel("ω")
plt.ylabel("|F(ω)|²")

# Дискретизація
plt.subplot(3,1,3)
plt.plot(t, f)
plt.stem(t_samples, f_samples)
plt.title("Дискретизація сигналу")
plt.xlabel("t")
plt.ylabel("f(t)")

plt.tight_layout()
plt.show()