import flet as ft
import numpy as np

def simpson_13(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("El número de subintervalos debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    integral = y[0] + y[-1] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2])
    integral *= h / 3
    
    return integral

def crear_componente():
    input_func = ft.TextField(label="Función f(x)", hint_text="Ej: np.sin(x)", expand=True)
    input_a = ft.TextField(label="Límite inferior a", hint_text="Ej: 0")
    input_b = ft.TextField(label="Límite superior b", hint_text="Ej: 3.14")
    input_n = ft.TextField(label="Subintervalos (par)", hint_text="Ej: 4")
    resultado_text = ft.Text("")
    
    def calcular_integral(e):
        try:
            expr = input_func.value
            a = float(input_a.value)
            b = float(input_b.value)
            n = int(input_n.value)
            
            if n % 2 != 0:
                resultado_text.value = "El número de subintervalos debe ser par."
                return

            f = lambda x: eval(expr, {"np": np, "x": x})
            resultado = simpson_13(f, a, b, n)
            resultado_text.value = f"Resultado de la integral ≈ {resultado:.6f}"
        except Exception as ex:
            resultado_text.value = f"Error: {str(ex)}"
        finally:
            e.page.update()
    
    return ft.Column([
        ft.Text("Método de Simpson 1/3", style="headlineSmall"),
        input_func,
        input_a,
        input_b,
        input_n,
        ft.ElevatedButton("Calcular", on_click=calcular_integral),
        resultado_text
    ])
