import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j1

x = np.linspace(-5, 5, 4000)
nu = np.linspace(-5, 5, 4000)

def rect(x):
    return np.where(np.abs(x) <= 0.5, 1, 0)

def sinc(x):
    return np.where(x == 0, 1, np.sin(np.pi*x)/(np.pi*x))

def triangle(x):
    return np.where(np.abs(x) <= 1, 1 - np.abs(x), 0)

def comb(x, period=1):
    result = np.zeros_like(x)
    for n in range(-5, 6):
        result += np.where(np.abs(x-n*period) < 0.01, 1, 0)
    return result

def sgn(x):
    return np.sign(x)

# ---------- 1 rect ----------
plt.figure()
plt.subplot(1,2,1)
plt.plot(x, rect(x))
plt.title("rect(x)")

plt.subplot(1,2,2)
plt.plot(nu, sinc(nu))
plt.title("Spectrum")
plt.show()

# ---------- 2 sinc ----------
plt.figure()
plt.subplot(1,2,1)
plt.plot(x, sinc(x))
plt.title("sinc(x)")

plt.subplot(1,2,2)
plt.plot(nu, rect(nu))
plt.title("Spectrum")
plt.show()

# ---------- 3 triangle ----------
plt.figure()
plt.subplot(1,2,1)
plt.plot(x, triangle(x))
plt.title("Λ(x)")

plt.subplot(1,2,2)
plt.plot(nu, sinc(nu)**2)
plt.title("Spectrum")
plt.show()

# ---------- 4 comb ----------
plt.figure()
plt.subplot(1,2,1)
plt.plot(x, comb(x))
plt.title("comb(x)")

plt.subplot(1,2,2)
plt.plot(nu, comb(nu))
plt.title("Spectrum")
plt.show()

# ---------- 5 sgn ----------
plt.figure()
plt.subplot(1,2,1)
plt.plot(x, sgn(x))
plt.title("sgn(x)")

plt.subplot(1,2,2)
plt.plot(nu, np.where(nu!=0, 1/(np.pi*nu), 0))
plt.title("Spectrum")
plt.show()

# ---------- 6 circ ----------
grid = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(grid, grid)
R = np.sqrt(X**2 + Y**2)
circ = np.where(R <= 1, 1, 0)

rho = np.sqrt(X**2 + Y**2)
spectrum = np.where(rho!=0, j1(2*np.pi*rho)/rho, np.pi)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(circ, extent=[-2,2,-2,2])
plt.title("circ(r)")

plt.subplot(1,2,2)
plt.imshow(spectrum, extent=[-2,2,-2,2])
plt.title("Spectrum")
plt.show()