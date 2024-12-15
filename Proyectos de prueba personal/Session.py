import Encriptado, flet

def main(page: flet.Page):
    page.add(flet.Text("Hello, world!"))
    page.add(flet.Text("Ingrese la longitud de la contraseña: "))
    page.add(flet.ElevatedButton("Generar", on_click=Encriptado.generate()))
    page.add(flet.ElevatedButton("Encriptar", on_click=Encriptado.encrypt))
    page.update()
flet.app(target=main)



