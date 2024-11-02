# Autor:Patricia Zaragoza Palma
# Ingenieria en Sistemas Computacionales

import sympy as sp
import tkinter as tk
from tkinter import messagebox

# Función para calcular la integral y mostrarla en un formato legible
def calcular_integral():
    funcion_str = entrada_funcion.get()
    try:
        # Definir la variable simbólica
        x = sp.symbols('x')
        # Convertir la función a una expresión simbólica
        funcion = sp.sympify(funcion_str)
        # Calcular la integral indefinida
        integral = sp.integrate(funcion, x)
        # Mostrar el resultado en notación matemática
        resultado = sp.pretty(integral + sp.symbols('C'))  # Agregamos la constante de integración
        # Actualizar la etiqueta con el resultado
        salida_integral.config(text=f"Integral: ∫ {funcion_str} dx = {resultado}")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al calcular la integral: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Integrales")

# Crear y colocar los elementos de la interfaz
etiqueta_funcion = tk.Label(ventana, text="Introduce la función a integrar:")
etiqueta_funcion.pack()

entrada_funcion = tk.Entry(ventana, width=40)
entrada_funcion.pack()

boton_calcular = tk.Button(ventana, text="Calcular Integral", command=calcular_integral)
boton_calcular.pack()

salida_integral = tk.Label(ventana, text="Integral: ")
salida_integral.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
