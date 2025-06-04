import numpy as np
import matplotlib.pyplot as plt

def graficas(x_d, y_d, x_size=12, y_size=12, dpi=110):
    plt.figure(figsize=(x_size, y_size), dpi=dpi)

    plt.subplot(331)
    plt.plot(x_d, y_d,"bo")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.subplot(332)
    plt.plot(x_d, np.sqrt(y_d),"bo")
    plt.xlabel("X")
    plt.ylabel("$\sqrt{y}$")

    plt.subplot(333)
    plt.plot(x_d, 1/y_d,"bo")
    plt.xlabel("X")
    plt.ylabel("$1/y$")

    plt.subplot(334)
    plt.plot(x_d**2, y_d,"bo")
    plt.xlabel("$x^2$")
    plt.ylabel("Y")

    plt.subplot(335)
    plt.plot(x_d**3, y_d,"bo")
    plt.xlabel("$x^3$")
    plt.ylabel("Y")

    plt.subplot(336)
    plt.plot(np.log(x_d), y_d,"bo")
    plt.xlabel("$Ln(x)$")
    plt.ylabel("Y")

    plt.subplot(337)
    plt.plot(x_d, np.log(y_d),"bo")
    plt.xlabel("X")
    plt.ylabel("$Ln(y)$")

    plt.subplot(338)
    plt.plot(np.sqrt(x_d), y_d,"bo")
    plt.xlabel("$\sqrt{x}$")
    plt.ylabel("Y")

    plt.subplot(339)
    plt.plot(np.log(x_d), np.log(y_d),"bo")
    plt.xlabel("$Ln(x)$")
    plt.ylabel("$Ln(y)$")

    plt.tight_layout()
    plt.show()

x_vals = np.array([1, 2, 3, 4, 5])
y_vals = x_vals**2 + 3*x_vals + 2

graficas(x_vals, y_vals)
