import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definición de la EDO para el inciso c: y' = -x^2 + sin(y)
def f(x, y):
    return -x**2 + np.sin(y)

# 2. Configuración de la malla para el campo de pendientes
x_vals = np.linspace(-4, 4, 25)
y_vals = np.linspace(-4, 4, 25)
X, Y = np.meshgrid(x_vals, y_vals)

DY = f(X, Y)
DX = np.ones_like(DY)

# Normalizar vectores
N = np.hypot(DX, DY)
DX_norm = DX / N
DY_norm = DY / N

# 3. Gráfica
plt.figure(figsize=(8, 6))

# Campo de pendientes con flechas
plt.quiver(
    X, Y, DX_norm, DY_norm, 
    color='gray', 
    alpha=0.6, 
    pivot='middle',
    scale=30,
    headwidth=3.5,
    headlength=4,
    headaxislength=3.5
)

# --- FAMILIA DE SOLUCIONES ---
x_eval_der = np.linspace(0, 4, 150)
x_eval_izq = np.linspace(0, -4, 150)

for y0_val in np.linspace(-3, 3, 7):
    sol_der = solve_ivp(f, (0, 4), [y0_val], t_eval=x_eval_der)
    sol_izq = solve_ivp(f, (0, -4), [y0_val], t_eval=x_eval_izq)
    
    x_total = np.concatenate((sol_izq.t[::-1], sol_der.t))
    y_total = np.concatenate((sol_izq.y[0][::-1], sol_der.y[0]))
    
    plt.plot(x_total, y_total, color='green', linestyle='--', alpha=0.7)

# --- SOLUCIÓN PARTICULAR PVI: Elegida y(0) = 0 ---
x0, y0 = 0, 0

sol_p_der = solve_ivp(f, (x0, 4), [y0], t_eval=np.linspace(x0, 4, 200))
sol_p_izq = solve_ivp(f, (x0, -4), [y0], t_eval=np.linspace(x0, -4, 200))

x_part = np.concatenate((sol_p_izq.t[::-1], sol_p_der.t))
y_part = np.concatenate((sol_p_izq.y[0][::-1], sol_p_der.y[0]))

# Graficar curva particular y punto inicial
plt.plot(x_part, y_part, 'r-', linewidth=2.5, label=f'Solución PVI elegida: y({x0})={y0}')
plt.plot(x0, y0, 'ro', markersize=8)

# Formato visual
plt.title(r"Inciso c) Campo de pendientes para $y' = -x^2 + \sin(y)$")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

# Guardar la imagen
plt.savefig("inciso_c.png", dpi=300)
print("¡Gráfica guardada exitosamente como inciso_c.png!")