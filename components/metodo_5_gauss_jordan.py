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

    return A  # <-- ¡Devolvemos TODA la matriz reducida!

def crear_componente():
    # Crear entradas en el orden que quieres: fila por fila
    entradas = [ft.TextField(width=70, text_align=ft.TextAlign.CENTER) for _ in range(12)]
    resultado_text = ft.Text("")
    
    def resolver_matriz(e):
        try:
            # Verificar que no haya campos vacíos
            if any(celda.value.strip() == "" for celda in entradas):
                resultado_text.value = "Por favor, llena todos los campos."
                e.page.update()
                return
            
            # Construir matriz
            matriz = [
                [float(entradas[0].value), float(entradas[1].value), float(entradas[2].value), float(entradas[3].value)],
                [float(entradas[4].value), float(entradas[5].value), float(entradas[6].value), float(entradas[7].value)],
                [float(entradas[8].value), float(entradas[9].value), float(entradas[10].value), float(entradas[11].value)],
            ]
            
            resultado = gauss_jordan(matriz)
            resultado_formateado = "\n".join(
                "  ".join(f"{valor:8.4f}" for valor in fila) for fila in resultado
            )
            resultado_text.value = f"Matriz reducida:\n{resultado_formateado}"
        
        except Exception as ex:
            resultado_text.value = f"Error: {str(ex)}"
        finally:
            e.page.update()

    # Organizar inputs como matriz 3x4 (3 filas de 4 columnas)
    matriz_ui = ft.Column([
        ft.Row(entradas[0:4], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(entradas[4:8], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(entradas[8:12], alignment=ft.MainAxisAlignment.CENTER),
    ], alignment=ft.MainAxisAlignment.CENTER)

    return ft.Column([
        ft.Text("Método de Eliminación de Gauss-Jordan (3x3)", style="headlineSmall"),
        ft.Text("Introduce los coeficientes A|b organizados:"),
        matriz_ui,
        ft.ElevatedButton("Resolver", on_click=resolver_matriz),
        resultado_text
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
