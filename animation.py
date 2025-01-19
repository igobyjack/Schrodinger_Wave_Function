from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

def animate_complex_matrix(matrix, x, ax=None, interval=50):
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    real_line, = ax.plot([], [], lw=2, label="Real Part", color="blue")
    imag_line, = ax.plot([], [], lw=2, label="Imaginary Part", color="orange")
    modulus_line, = ax.plot([], [], lw=2, label="Modulus", color="black")

    ax.set_xlim(min(x), max(x))

    all_values = np.array(matrix).flatten()
    y_min = min(np.min(all_values.real), np.min(all_values.imag))
    y_max = max(np.max(all_values.real), np.max(all_values.imag))
    ax.set_ylim(y_min, y_max)
    ax.legend()

    def update(frame):
        y_real = np.real(matrix[frame])
        y_imag = np.imag(matrix[frame])
        y_modulus = np.abs(matrix[frame])

        # Update lines
        real_line.set_data(x, y_real)
        imag_line.set_data(x, y_imag)
        modulus_line.set_data(x, y_modulus)

        return real_line, imag_line, modulus_line

    ani = FuncAnimation(fig, update, frames=len(matrix), blit=False, interval=interval)
    
    return ani  