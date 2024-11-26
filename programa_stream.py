import streamlit as st
import numpy as np
import plotly.graph_objects as go

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

# Gráfico del ejercicio 1 con plotly
x = np.linspace(-1, 4, 500)
f = x**2 - 4 * x + 5
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=f, mode='lines', name=r"$f(x) = x^2 - 4x + 5$", line=dict(color='blue')))
fig.add_trace(go.Scatter(x=[2], y=[1], mode='markers', name="Mínimo global en $(2, 1)$", marker=dict(color='red', size=10)))
fig.update_layout(
    title="Gráfica de $f(x) = x^2 - 4x + 5$",
    xaxis_title="$x$",
    yaxis_title="$f(x)$",
    showlegend=True
)
st.plotly_chart(fig)

# Ejercicio 2: Función absoluta
st.header("2. Determinar si $f(x) = |x|$ tiene un mínimo global o local")
st.write("La función $f(x) = |x|$ tiene un mínimo global en $x = 0$ con $f(0) = 0$, ya que es el valor más bajo posible.")

# Gráfico del ejercicio 2 con plotly
x = np.linspace(-2, 2, 500)
f_abs = np.abs(x)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=f_abs, mode='lines', name=r"$f(x) = |x|$", line=dict(color='green')))
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', name="Mínimo global en $(0, 0)$", marker=dict(color='red', size=10)))
fig.update_layout(
    title="Gráfica de $f(x) = |x|$",
    xaxis_title="$x$",
    yaxis_title="$f(x)$",
    showlegend=True
)
st.plotly_chart(fig)

# Ejercicio 3: Función seno y Teorema de Weierstrass
st.header("3. Aplicación del Teorema de Weierstrass en $f(x) = \sin(x)$ en $[0, \pi]$")
st.write("La función $f(x) = \sin(x)$ tiene un mínimo global en $x = 0$ y $x = \pi$, donde $f(x) = 0$.")
st.write("El máximo global ocurre en $x = \pi/2$, donde $f(x) = 1$.")

# Gráfico del ejercicio 3 con plotly
x = np.linspace(0, np.pi, 500)
f_sin = np.sin(x)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=f_sin, mode='lines', name=r"$f(x) = \sin(x)$", line=dict(color='orange')))
fig.add_trace(go.Scatter(x=[0, np.pi], y=[0, 0], mode='markers', name="Mínimos globales en $x = 0$ y $x = \pi$", marker=dict(color='red', size=10)))
fig.add_trace(go.Scatter(x=[np.pi/2], y=[1], mode='markers', name="Máximo global en $x = \pi/2$", marker=dict(color='blue', size=10)))
fig.update_layout(
    title="Gráfica de $f(x) = \sin(x)$ en $[0, \pi]$",
    xaxis_title="$x$",
    yaxis_title="$f(x)$",
    showlegend=True
)
st.plotly_chart(fig)

# Ejercicio 4: Función en dos variables
st.header("4. Mínimo global de $f(x, y) = x^2 + y^2$ con $x^2 + y^2 \leq 1$")
st.write("La función alcanza su mínimo global en $(x, y) = (0, 0)$ con $f(0, 0) = 0$.")
st.write("El dominio está restringido al círculo $x^2 + y^2 \leq 1$.")

# Gráfico del ejercicio 4 en 2D con plotly
theta = np.linspace(0, 2 * np.pi, 500)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='lines', name="Dominio $x^2 + y^2 \leq 1$", fill='toself', fillcolor='lightblue'))
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', name="Mínimo global $(0, 0)$", marker=dict(color='red', size=10)))
fig.update_layout(
    title="Dominio y mínimo global en $f(x, y) = x^2 + y^2$",
    xaxis_title="$x$",
    yaxis_title="$y$",
    showlegend=True
)
st.plotly_chart(fig)

# Ejercicio 5: Ejemplo con mínimo global no único
st.header("5. Ejemplo donde un mínimo global no sea único")
st.write("Un ejemplo es la función $f(x, y) = x^2 + y^2$ restringida al círculo $x^2 + y^2 = 1$.")
st.write("En este caso, el mínimo global ocurre en todos los puntos del círculo, ya que $f(x, y) = 1$ para cualquier $(x, y)$ en el borde.")

# Gráfico del ejercicio 5 con plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='lines', name="Círculo $x^2 + y^2 = 1$", line=dict(color='purple')))
fig.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='markers', name="Mínimos globales", marker=dict(color='purple', size=5)))
fig.update_layout(
    title="Ejemplo: Mínimos globales en el círculo $x^2 + y^2 = 1$",
    xaxis_title="$x$",
    yaxis_title="$y$",
    showlegend=True
)
st.plotly_chart(fig)
