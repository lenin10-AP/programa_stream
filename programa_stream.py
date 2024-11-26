import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Optimización no lineal", layout="wide")

st.title("Resolución de Ejercicios de Optimización No Lineal")
st.write("Este programa resuelve paso a paso los ejercicios planteados de optimización no lineal.")

# Ejercicio 1: Verificar minimizadores locales y globales
st.header("1. Verificar minimizadores para $f(x) = x^2 - 4x + 5$")
st.write("### Función: $f(x) = x^2 - 4x + 5$")
st.latex(r"f'(x) = 2x - 4 \quad \Rightarrow \quad x = 2")
st.write("El punto crítico es $x = 2$. Evaluando:")
st.latex(r"f(2) = 2^2 - 4(2) + 5 = 1")
st.write("El mínimo global ocurre en $x = 2$ con valor $f(2) = 1$. Evaluemos en $x = 0$: ")
st.latex(r"f(0) = 0^2 - 4(0) + 5 = 5")

# Gráfico del ejercicio 1
x = np.linspace(-1, 4, 500)
f = x**2 - 4 * x + 5
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, f, label=r"$f(x) = x^2 - 4x + 5$", color="blue")
ax.scatter(2, 1, color="red", label="Mínimo global en $(2, 1)$")
ax.axhline(0, color="black", linestyle="--")
ax.axvline(0, color="black", linestyle="--")
ax.legend()
ax.set_title("Gráfica de $f(x) = x^2 - 4x + 5$")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")
st.pyplot(fig)

# Ejercicio 2: Función absoluta
st.header("2. Determinar si $f(x) = |x|$ tiene un mínimo global o local")
st.write("La función $f(x) = |x|$ tiene un mínimo global en $x = 0$ con $f(0) = 0$, ya que es el valor más bajo posible.")

# Gráfico del ejercicio 2
x = np.linspace(-2, 2, 500)
f_abs = np.abs(x)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, f_abs, label=r"$f(x) = |x|$", color="green")
ax.scatter(0, 0, color="red", label="Mínimo global en $(0, 0)$")
ax.axhline(0, color="black", linestyle="--")
ax.axvline(0, color="black", linestyle="--")
ax.legend()
ax.set_title("Gráfica de $f(x) = |x|$")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")
st.pyplot(fig)

# Ejercicio 3: Función seno y Teorema de Weierstrass
st.header("3. Aplicación del Teorema de Weierstrass en $f(x) = \sin(x)$ en $[0, \pi]$")
st.write("La función $f(x) = \sin(x)$ tiene un mínimo global en $x = 0$ y $x = \pi$, donde $f(x) = 0$.")
st.write("El máximo global ocurre en $x = \pi/2$, donde $f(x) = 1$.")

# Gráfico del ejercicio 3
x = np.linspace(0, np.pi, 500)
f_sin = np.sin(x)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, f_sin, label=r"$f(x) = \sin(x)$", color="orange")
ax.scatter([0, np.pi], [0, 0], color="red", label="Mínimos globales en $x = 0$ y $x = \pi$")
ax.scatter(np.pi / 2, 1, color="blue", label="Máximo global en $x = \pi/2$")
ax.axhline(0, color="black", linestyle="--")
ax.axvline(0, color="black", linestyle="--")
ax.legend()
ax.set_title("Gráfica de $f(x) = \sin(x)$ en $[0, \pi]$")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")
st.pyplot(fig)

# Ejercicio 4: Función en dos variables
st.header("4. Mínimo global de $f(x, y) = x^2 + y^2$ con $x^2 + y^2 \leq 1$")
st.write("La función alcanza su mínimo global en $(x, y) = (0, 0)$ con $f(0, 0) = 0$.")
st.write("El dominio está restringido al círculo $x^2 + y^2 \leq 1$.")

# Gráfico del ejercicio 4 en 2D
theta = np.linspace(0, 2 * np.pi, 500)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

fig, ax = plt.subplots(figsize=(5, 3))
ax.fill(x_circle, y_circle, color="lightblue", alpha=0.5, label="Dominio $x^2 + y^2 \leq 1$")
ax.scatter(0, 0, color="red", label="Mínimo global $(0, 0)$")
ax.axhline(0, color="black", linestyle="--")
ax.axvline(0, color="black", linestyle="--")
ax.set_aspect("equal")
ax.set_title("Dominio y mínimo global en $f(x, y) = x^2 + y^2$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
st.pyplot(fig)

# Ejercicio 5: Ejemplo con mínimo global no único
st.header("5. Ejemplo donde un mínimo global no sea único")
st.write("Un ejemplo es la función $f(x, y) = x^2 + y^2$ restringida al círculo $x^2 + y^2 = 1$.")
st.write("En este caso, el mínimo global ocurre en todos los puntos del círculo, ya que $f(x, y) = 1$ para cualquier $(x, y)$ en el borde.")

# Gráfico del ejercicio 5
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x_circle, y_circle, label="Círculo $x^2 + y^2 = 1$", color="purple")
ax.scatter(x_circle, y_circle, color="purple", s=5, label="Mínimos globales")
ax.set_title("Ejemplo: Mínimos globales en el círculo $x^2 + y^2 = 1$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
ax.set_aspect("equal")
st.pyplot(fig)
