import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Lorentz eq
def func_lorenz(var, t, p, r, b):
    dxdt = -p*var[0] + p*var[1]
    dydt = -var[0]*var[2] + r*var[0] - var[1]
    dzdt = var[0]*var[1] - b*var[2]
    
    return [dxdt, dydt, dzdt]

# 3D visualization
def plot3d(var_list):
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_zlabel("$z$")
    ax.plot(var_list[:, 0], var_list[:, 1], var_list[:, 2], color="m", linewidth=0.5, label="dxdt = -px + py\ndydt = -xz + rx - y\ndzdt = xy - bz")
    
    plt.legend()
    plt.show()

def main():
    t_list = np.linspace(0.0, 100.0, 10000)
    p = 10
    r = 28
    b = 8/3
    var_init = [0.1, 0.1, 0.1]
    var_list = odeint(func_lorenz, var_init, t_list, args = (p, r, b))
    
    plot3d(var_list)
    
if __name__ == '__main__':
    main()