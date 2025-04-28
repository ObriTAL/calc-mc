import flet as ft

def gauss_jordan(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        # Pivoteo: asegurar que el elemento diagonal sea 1
        divisor = matrix[i][i]
        if divisor == 0:
            return "No se puede dividir por cero (pivot 0)."
        for j in range(cols):
            matrix[i][j] /= divisor

        # Eliminar otras filas
        for k in range(rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(cols):
                    matrix[k][j] -= factor * matrix[i][j]
    
    return matrix


def EnhancedMatrixComponent():
    rows_dropdown = ft.Dropdown(
        label="Filas",
        options=[ft.dropdown.Option("2"), ft.dropdown.Option("3")],
        value="3",
        width=100
    )
    cols_dropdown = ft.Dropdown(
        label="Columnas",
        options=[ft.dropdown.Option("3"), ft.dropdown.Option("4")],
        value="4",
        width=100
    )

    matrix_inputs = []
    matrix_grid = ft.Column()
    result_area = ft.Text(color=ft.colors.GREEN_200)

    def update_matrix_inputs(e=None):
        matrix_inputs.clear()
        matrix_grid.controls.clear()

        rows = int(rows_dropdown.value)
        cols = int(cols_dropdown.value)
        for i in range(rows):
            row_inputs = []
            row = ft.Row()
            for j in range(cols):
                field = ft.TextField(
                    width=70, 
                    height=40, 
                    text_align=ft.TextAlign.CENTER,
                    keyboard_type=ft.KeyboardType.NUMBER
                )
                row.controls.append(field)
                row_inputs.append(field)
            matrix_inputs.append(row_inputs)
            matrix_grid.controls.append(row)
        page.update()

    def solve(e):
        try:
            matrix = [
                [float(cell.value) if cell.value else 0 for cell in row]
                for row in matrix_inputs
            ]
            result = gauss_jordan(matrix)
            if isinstance(result, str):
                result_area.value = f"Error: {result}"
            else:
                result_str = "\n".join(["\t".join(f"{val:.4f}" for val in row) for row in result])
                result_area.value = f"Resultado:\n{result_str}"
        except Exception as ex:
            result_area.value = f"Error al procesar: {ex}"
        result_area.update()

    update_matrix_inputs()  # Inicial

    return ft.Column([
        ft.Row([
            rows_dropdown,
            cols_dropdown,
            ft.ElevatedButton("Actualizar", on_click=update_matrix_inputs)
        ]),
        ft.Text("Ingrese los valores de la matriz aumentada (Ax=b):", color=ft.colors.WHITE),
        matrix_grid,
        ft.ElevatedButton("Resolver por Gauss-Jordan", on_click=solve),
        result_area
    ])