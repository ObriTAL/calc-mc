import flet as ft
import numpy as np

def gauss_jordan(matriz):
    n = len(matriz)
    A = np.array(matriz, dtype=float)

    for i in range(n):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[[i, j]] = A[[j, i]]
                    break

        A[i] = A[i] / A[i][i]

        for j in range(n):
            if i != j:
                A[j] = A[j] - A[j][i] * A[i]

    return A

def crear_componente():
    entradas = []
    matriz_ui = ft.Column()
    resultado_text = ft.Text("")
    tamaño_matriz = ft.TextField(label="Tamaño de la matriz (N)", width=100)
    
    def generar_matriz(e):
        nonlocal entradas
        entradas.clear()
        matriz_ui.controls.clear()

        try:
            n = int(tamaño_matriz.value)
            if n < 2 or n > 10:
                resultado_text.value = "Por favor ingresa un número entre 2 y 10."
                e.page.update()
                return

            for _ in range(n * (n + 1)):  # Incluyendo columna de resultados
                entradas.append(ft.TextField(width=60, text_align=ft.TextAlign.CENTER))

            for i in range(n):
                fila = ft.Row(
                    entradas[i*(n+1):(i+1)*(n+1)],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
                matriz_ui.controls.append(fila)

            resultado_text.value = ""

        except ValueError:
            resultado_text.value = "Por favor ingresa un número válido."
        
        e.page.update()

    def resolver_matriz(e):
        try:
            if any(celda.value.strip() == "" for celda in entradas):
                resultado_text.value = "Por favor, llena todos los campos."
                e.page.update()
                return

            n = int(tamaño_matriz.value)
            matriz = []
            for i in range(n):
                fila = [float(entradas[i*(n+1) + j].value) for j in range(n+1)]
                matriz.append(fila)

            resultado = gauss_jordan(matriz)
            resultado_formateado = "\n".join(
                "  ".join(f"{valor:8.4f}" for valor in fila) for fila in resultado
            )
            resultado_text.value = f"Matriz reducida:\n{resultado_formateado}"

        except Exception as ex:
            resultado_text.value = f"Error: {str(ex)}"
        
        e.page.update()

    return ft.Column([
        ft.Text("Gauss-Jordan para Matrices NxN", style="headlineSmall"),
        ft.Row([
            tamaño_matriz,
            ft.ElevatedButton("Generar matriz", on_click=generar_matriz),
        ], alignment=ft.MainAxisAlignment.CENTER),
        matriz_ui,
        ft.ElevatedButton("Resolver", on_click=resolver_matriz),
        resultado_text
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
