#programa basico que muestra un hola mundo en un label en una interfaz grafica flet

import flet as ft

def main(page: ft.Page):
    #Definimos el contenido de la pagina
    page.add(ft.Text("Hello, world!"))
    #definir el tamaño de la pagina y centrarlo en una sola linea de codigo
    page.window_width = 600
    page.window_height = 400
    page.window_center()
    #agregar un boton
    page.add(ft.ElevatedButton("Tocame", on_click=lambda _: page.dialog(content=ft.Text("Hello, world!"), modal=True)))

    page.update()

ft.app(target=main)


#componente de la interfaz grafica que mostrara un modal con un mensaje, que se activa al ser presionado un boton
