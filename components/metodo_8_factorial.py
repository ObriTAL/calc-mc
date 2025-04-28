import flet as ft
import math

def calcular_factorial(n):
    return math.factorial(n)

def crear_componente():
    input_numero = ft.TextField(label="Número para calcular el factorial", width=300)
    resultado_texto = ft.Text("Resultado: ", size=20)

    def calcular_click(e):
        try:
            n = int(input_numero.value)
            if n < 0:
                raise ValueError("El número debe ser no negativo.")
            resultado = calcular_factorial(n)
            resultado_texto.value = f"{n}! = {resultado}"
        except Exception as ex:
            resultado_texto.value = f"Error: {ex}"
        input_numero.value = ""
        input_numero.focus()
        e.control.page.update()

    boton_calcular = ft.ElevatedButton(text="Calcular Factorial", on_click=calcular_click)

    return ft.Column(
        controls=[
            ft.Text("Calculadora de Factorial", size=30, weight=ft.FontWeight.BOLD),
            input_numero,
            boton_calcular,
            resultado_texto,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
