import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definición de la EDO: y' = -y - sin(x)
def f(x, y):
    return -y - np.sin(x)

# 2. Configuración de la malla para el campo de pendientes
x_vals = np.linspace(-4, 4, 25)
y_vals = np.linspace(-4, 4, 25)
X, Y = np.meshgrid(x_vals, y_vals)

DY = f(X, Y)
DX = np.ones_like(DY)

# Normalizar segmentos
N = np.hypot(DX, DY)
DX_norm = DX / N
DY_norm = DY / N

# 3. Gráfica
plt.figure(figsize=(8, 6))

# Campo de pendientes CON CABEZAS DE FLECHA
plt.quiver(
    X, Y, DX_norm, DY_norm, 
    color='gray', 
    alpha=0.6, 
    pivot='middle',
    scale=30,             # Escala de tamaño de las flechas
    headwidth=3.5,        # Ancho de la cabeza de la flecha
    headlength=4,         # Longitud de la cabeza
    headaxislength=3.5    # Forma de la base de la flecha
)

# Rango de integración
x_span = (-4, 4)
x_eval = np.linspace(-4, 4, 300)

# Familia de soluciones (curvas secundarias en el fondo)
for y0_val in np.linspace(-3, 3, 7):
    sol = solve_ivp(f, x_span, [y0_val], t_eval=x_eval)
    plt.plot(sol.t, sol.y[0], color='green', linestyle='--', alpha=0.7)

# Solución particular para y(0) = 1
x0, y0 = 0, 1
sol_particular = solve_ivp(f, x_span, [y0], t_eval=x_eval)

# Graficar solución particular y punto inicial
plt.plot(sol_particular.t, sol_particular.y[0], 'r-', linewidth=2.5, label=f'Solución PVI: y({x0})={y0}')
plt.plot(x0, y0, 'ro', markersize=8)

# Formato de la gráfica
plt.title(r"Inciso a) Campo de pendientes para $y' = -y - \sin(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

# Guardar la imagen
plt.savefig("inciso_a.png", dpi=300)
print("¡Gráfica actualizada con flechas y guardada como inciso_a.png!")