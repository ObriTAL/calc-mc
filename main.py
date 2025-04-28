import flet as ft
from importlib import import_module


metodos = [
    ("Newton-Raphson", "metodo_2_newton"),   #Joss
    ("Serie de Taylor", "metodo_3_taylor"),  #Rodrigo
    ("Simpson 1/3", "metodo_4_simpson"),     #Ebroin
    ("Gauss-Jordan", "metodo_5_gauss_jordan"),#Gael
    ("Matriz NxN", "metodo_6_nxn"),           #Pelon
    ("Euler", "metodo_7_euler"),              #Lexus
    ("Serie Aritmética", "metodo_11_serie_aritmetica"), #Marco
    ("Factorial", "metodo_8_factorial"), #Ricardo
    ("Simpson", "metodo_9_simpson"),
    ("Romberg", "metodo_10_romberg"),
]

def main(page: ft.Page):
    page.title = "Calculadora de Métodos Numéricos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.GREY_100
    page.window_maximized = True
    page.scroll = ft.ScrollMode.AUTO

    contenedor_metodo = ft.Container(
        expand=True,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        padding=20,
        animate=ft.animation.Animation(400, "ease"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.BLACK12,
            offset=ft.Offset(0, 5),
        ),
    )

    def cambiar_metodo(index):
        try:
            nombre_modulo = metodos[index][1]
            modulo = import_module(f"components.{nombre_modulo}")
            componente = modulo.crear_componente()
            contenedor_metodo.content = componente
            page.update()
        except Exception as e:
            contenedor_metodo.content = ft.Text(f"Error cargando componente: {e}", color="red")
            page.update()

    menu_lateral = ft.Container(
        width=250,
        bgcolor=ft.colors.RED_600,
        border_radius=15,
        padding=10,
        margin=10,
        content=ft.Column(
            controls=[
                ft.Text("Métodos", size=30, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                *[
                    ft.Container(
                        content=ft.TextButton(
                            text=nombre,
                            style=ft.ButtonStyle(
                                color={"": ft.colors.WHITE, "hovered": ft.colors.RED_800},
                                bgcolor={"": ft.colors.RED_600, "hovered": ft.colors.RED_200},
                                overlay_color=ft.colors.RED_100,
                                shape=ft.RoundedRectangleBorder(radius=10),
                                animation_duration=400,
                            ),
                            on_click=lambda e, i=i: cambiar_metodo(i),
                        ),
                        margin=ft.margin.only(bottom=5),
                        animate=ft.animation.Animation(400, "easeInOut"),
                    )
                    for i, (nombre, _) in enumerate(metodos)
                ]
            ],
            scroll=ft.ScrollMode.AUTO,
        ),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.colors.BLACK12,
            offset=ft.Offset(0, 5),
        ),
    )

    page.add(
        ft.Row(
            controls=[
                menu_lateral,
                contenedor_metodo,
            ],
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    )

ft.app(target=main)
