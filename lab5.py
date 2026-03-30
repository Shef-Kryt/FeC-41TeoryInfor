n = 237

print("Binary:", bin(n))
print("Octal:", oct(n))
print("Hex:", hex(n))
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.01, 1000)

A = 4
m = 0.35
fc = 1000
fm = 100

s = A*(1 + m*np.cos(2*np.pi*fm*t))*np.cos(2*np.pi*fc*t)

plt.plot(t, s)
plt.title("AM сигнал")
plt.xlabel("t")
plt.ylabel("s(t)")
plt.show()



fc = 120000
fm = np.linspace(300, 3400, 100)

plt.figure()

plt.stem([fc], [1])
plt.stem(fc + fm, np.ones_like(fm)*0.5)
plt.stem(fc - fm, np.ones_like(fm)*0.5)

plt.title("Спектр AM сигналу")
plt.xlabel("Частота")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

m = np.arange(0, 1.1, 0.1)
ratio = (m**2)/2

plt.plot(m, ratio*100)
plt.xlabel("m")
plt.ylabel("% потужності")
plt.title("Співвідношення потужностей")
plt.show()
import numpy as np

R = 10000
m = 0.4
f = 4000

omega = 2*np.pi*f

RC = np.sqrt(1-m**2)/(m*omega)
C = RC / R

print("C =", C)
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
digital = np.sign(np.sin(2*np.pi*2*t))

carrier = np.cos(2*np.pi*20*t)

# ASK
ask = (digital + 1)/2 * carrier

# PSK
psk = np.cos(2*np.pi*20*t + np.pi*(digital<0))

plt.figure()

plt.subplot(3,1,1)
plt.plot(t, digital)
plt.title("Цифровий сигнал")

plt.subplot(3,1,2)
plt.plot(t, ask)
plt.title("ASK")

plt.subplot(3,1,3)
plt.plot(t, psk)
plt.title("PSK")

plt.tight_layout()
plt.show()