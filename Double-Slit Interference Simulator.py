import numpy as np
import matplotlib.pyplot as plt
 
x=np.linspace(-0.05,0.05,1000)
D=2
a=0.1e-3
λ=500e-9
I0=1
i=(λ*D)/a   #or δ=(a*x)/D

plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
I=2*I0*(1+np.cos((2*np.pi*x)/i))    #or I=2*I0*(1+np.cos((2*np.pi*δ)/λ))
plt.plot(x, I, color="red")
plt.title("Intensity distribution")
plt.xlabel("x")
plt.ylabel("I(x)")
plt.legend()
plt.grid(True)
plt.xlim(-0.05,0.05)
plt.ylim(0,4)

plt.subplot(1, 2, 2)
I_2d = np.outer(I, np.ones(100))
plt.imshow(I_2d, extent=[0, 1, -0.05,0.05],cmap = "gray", aspect="auto")
plt.xlabel("y (m)")
plt.ylabel("x (m)")
plt.title("Interference fringes")
plt.show()