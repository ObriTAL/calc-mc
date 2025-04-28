import flet as ft
import math

def metodo_newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    resultados = []
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-10:
            resultados.append("Derivada casi cero. No se puede continuar.")
            break

        x_new = x - fx / dfx
        error = abs(x_new - x)

        resultados.append(f"Iteración {i + 1}: x = {x_new:.6f}, error = {error:.6e}")

        if error < tol:
            resultados.append(f"\nConvergencia alcanzada después de {i + 1} iteraciones.")
            break

        x = x_new
    else:
        resultados.append("Máximo de iteraciones alcanzado.")

    return resultados


def crear_componente():
    entrada_funcion = ft.TextField(label="f(x)", hint_text="Ej: x**2 - 2", expand=True)
    entrada_derivada = ft.TextField(label="f'(x)", hint_text="Ej: 2*x", expand=True)
    entrada_x0 = ft.TextField(label="x0 (valor inicial)", hint_text="Ej: 1.5", expand=True)
    salida = ft.Text("", selectable=True)

    def calcular(e):
        try:
            f = lambda x: eval(entrada_funcion.value, {"x": x, **vars(math)})
            df = lambda x: eval(entrada_derivada.value, {"x": x, **vars(math)})
            x0 = float(entrada_x0.value)

            resultados = metodo_newton_raphson(f, df, x0)
            salida.value = "\n".join(resultados)
            e.control.page.update()

        except Exception as error:
            salida.value = f"Error: {str(error)}"
            e.control.page.update()

    boton_calcular = ft.ElevatedButton(text="Calcular raíz", on_click=calcular)

    return ft.Column(
        controls=[
            ft.Text("Método de Newton-Raphson", style="headlineMedium"),
            entrada_funcion,
            entrada_derivada,
            entrada_x0,
            boton_calcular,
            salida
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
