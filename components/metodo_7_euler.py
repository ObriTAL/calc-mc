import flet as ft

def calcular_euler(n_terminos):
    euler = 0
    factorial = 1
    for n in range(n_terminos):
        if n != 0:
            factorial *= n
        euler += 1 / factorial
    return euler

def crear_componente():
    input_terminos = ft.TextField(label="Número de términos", width=300)
    resultado_texto = ft.Text("Resultado: ", size=20)

    def calcular_click(e):
        try:
            n = int(input_terminos.value)
            resultado = calcular_euler(n)
            resultado_texto.value = f"Valor aproximado de e: {resultado:.10f}"
        except Exception as ex:
            resultado_texto.value = f"Error: {ex}"
        input_terminos.value = ""
        input_terminos.focus()
        e.control.page.update()

    boton_calcular = ft.ElevatedButton(text="Calcular e", on_click=calcular_click)

    return ft.Column(
        controls=[
            ft.Text("Aproximación del número e", size=30, weight=ft.FontWeight.BOLD),
            input_terminos,
            boton_calcular,
            resultado_texto,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
