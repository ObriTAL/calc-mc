import flet as ft
import math

def derivada_numerica(f, x, orden=1, h=1e-5):
    if orden == 0:
        return f(x)
    elif orden == 1:
        return (f(x + h) - f(x - h)) / (2 * h)
    elif orden == 2:
        return (f(x + h) - 2*f(x) + f(x - h)) / (h ** 2)
    else:
        return (derivada_numerica(f, x + h, orden-1, h) - derivada_numerica(f, x - h, orden-1, h)) / (2 * h)

def taylor_series(f, a, x, n):
    suma = 0
    for i in range(n):
        deriv = derivada_numerica(f, a, orden=i)
        termino = (deriv * (x - a) ** i) / math.factorial(i)
        suma += termino
    return suma

def crear_componente():
    input_func = ft.TextField(label="Función f(x)", hint_text="Ej: math.sin(x)", expand=True)
    input_a = ft.TextField(label="Punto de expansión a", hint_text="Ej: 0")
    input_x = ft.TextField(label="Punto de evaluación x", hint_text="Ej: 0.5")
    input_n = ft.TextField(label="Número de términos", hint_text="Ej: 5")
    resultado_text = ft.Text("")
    
    def calcular_taylor(e):
        try:
            expr = input_func.value
            a = float(input_a.value)
            x = float(input_x.value)
            n = int(input_n.value)
            
            f = lambda x: eval(expr, {"math": math, "x": x})
            resultado = taylor_series(f, a, x, n)
            resultado_text.value = f"Resultado de la Serie de Taylor ≈ {resultado:.6f}"
        except Exception as ex:
            resultado_text.value = f"Error: {str(ex)}"
        finally:
            e.page.update()
    
    return ft.Column([
        ft.Text("Serie de Taylor", style="headlineSmall"),
        input_func,
        input_a,
        input_x,
        input_n,
        ft.ElevatedButton("Calcular", on_click=calcular_taylor),
        resultado_text
    ])
