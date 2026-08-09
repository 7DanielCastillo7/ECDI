import matplotlib.pyplot as plt

# Puntos críticos para y' = y*(3-y)*(y-2)
puntos_criticos = [0, 2, 3]
nombres_puntos = ['0', '2', '3']

# Intervalos e indicaciones de dirección (flechas)
intervalos = [
    (-1.0, 0, 'arriba'),   # y < 0: y' > 0 (sube)
    (0, 2, 'abajo'),       # 0 < y < 2: y' < 0 (baja)
    (2, 3, 'arriba'),      # 2 < y < 3: y' > 0 (sube)
    (3, 4.0, 'abajo')      # y > 3: y' < 0 (baja)
]

# Crear figura
plt.figure(figsize=(4, 8))

# 0. Título en la parte superior
plt.text(0, 5.0, 'Diagrama Fase', fontsize=16, fontweight='bold', ha='center', color='navy')

# 1. Dibujar el eje vertical y (recta de fase)
plt.plot([0, 0], [-1.2, 4.2], color='navy', linewidth=1.5, zorder=1)

# 2. Dibujar las flechas de dirección en los intervalos
for y_start, y_end, direccion in intervalos:
    y_mid = (y_start + y_end) / 2
    
    if direccion == 'arriba':
        plt.annotate(
            '', xy=(0, y_mid + 0.2), xytext=(0, y_mid - 0.2),
            arrowprops=dict(arrowstyle="->", color='navy', lw=2, mutation_scale=15)
        )
    else:  # abajo
        plt.annotate(
            '', xy=(0, y_mid - 0.2), xytext=(0, y_mid + 0.2),
            arrowprops=dict(arrowstyle="->", color='navy', lw=2, mutation_scale=15)
        )

# 3. Marcar los puntos críticos y sus etiquetas
for y_val, etiqueta in zip(puntos_criticos, nombres_puntos):
    # Marca horizontal sobre la recta
    plt.plot([-0.05, 0.05], [y_val, y_val], color='navy', linewidth=2)
    # Etiqueta del valor a la izquierda
    plt.text(-0.1, y_val, etiqueta, fontsize=12, va='center', ha='right', color='navy')

# 4. Etiqueta superior del eje
plt.text(0, 4.35, r'$eje\ y$', fontsize=13, ha='center', va='bottom', color='navy', fontstyle='italic')

# Configuración de límites y ocultar marco predeterminado
plt.xlim(-0.8, 0.8)
plt.ylim(-1.5, 5.4)
plt.axis('off')

# Guardar y mostrar
plt.tight_layout()
plt.savefig("diagrama_a.png", dpi=300, bbox_inches='tight')
plt.show()

print("¡Diagrama de fase con título generado exitosamente!")