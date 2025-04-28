import flet as ft

def crear_componente():
    a_input = ft.TextField(label="Primer término (a1)", keyboard_type=ft.KeyboardType.NUMBER)
    d_input = ft.TextField(label="Diferencia común (d)", keyboard_type=ft.KeyboardType.NUMBER)
    n_input = ft.TextField(label="Número de términos (n)", keyboard_type=ft.KeyboardType.NUMBER)
    k_input = ft.TextField(label="¿Qué término específico deseas calcular (k)?", keyboard_type=ft.KeyboardType.NUMBER)

    resultado_texto = ft.Text("")

    def calcular(e):
        try:
            a = float(a_input.value)
            d = float(d_input.value)
            n = int(float(n_input.value))
            k = int(float(k_input.value))

            termino_k = a + (k - 1) * d
            serie = [a + i * d for i in range(n)]
            suma = (n / 2) * (2 * a + (n - 1) * d)

            resultado_texto.value = (
                f"Término {k}: {termino_k}\n"
                f"Serie generada: {serie}\n"
                f"Suma de los primeros {n} términos: {suma}"
            )
        except Exception as ex:
            resultado_texto.value = f"Error: {ex}"

        resultado_texto.update()

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Serie Aritmética", size=30),
                a_input,
                d_input,
                n_input,
                k_input,
                ft.ElevatedButton("Calcular", on_click=calcular),
                resultado_texto
            ],
            scroll=ft.ScrollMode.AUTO
        ),
        padding=20
    )
