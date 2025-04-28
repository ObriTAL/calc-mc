import flet as ft

def crear_componente():
    numero1 = ft.TextField(label="Número 1", width=150, text_align=ft.TextAlign.CENTER)
    numero2 = ft.TextField(label="Número 2", width=150, text_align=ft.TextAlign.CENTER)
    operador = ft.Dropdown(
        label="Operación",
        width=150,
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/"),
        ]
    )
    resultado_text = ft.Text("", style="headlineSmall")

    def calcular(e):
        try:
            n1 = float(numero1.value)
            n2 = float(numero2.value)
            op = operador.value

            if op == "+":
                resultado = n1 + n2
            elif op == "-":
                resultado = n1 - n2
            elif op == "*":
                resultado = n1 * n2
            elif op == "/":
                if n2 == 0:
                    resultado_text.value = "Error: División entre cero"
                    e.page.update()
                    return
                resultado = n1 / n2
            else:
                resultado_text.value = "Selecciona una operación."
                e.page.update()
                return

            resultado_text.value = f"Resultado: {resultado:.4f}"
        except ValueError:
            resultado_text.value = "Error: Ingresa números válidos."
        
        e.page.update()

    return ft.Column([
        ft.Text("Calculadora Básica 🧮", style="headlineSmall"),
        ft.Row([numero1, operador, numero2], alignment=ft.MainAxisAlignment.CENTER),
        ft.ElevatedButton("Calcular", on_click=calcular),
        resultado_text
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
