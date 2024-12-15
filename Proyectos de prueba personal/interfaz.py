import flet as ft
from Encriptado import generate, encrypt  # Import specific functions

def main(page: ft.Page):
    length_slider = ft.Slider(min=8, max=32, divisions=24, label="{value}")
    password_text = ft.TextField(read_only=True)

    def generate_button_clicked(e):
        password = generate(int(length_slider.value))  # Use imported function
        encrypted_password = encrypt(password)  # Use imported function
        password_text.value = encrypted_password
        page.update()

    page.add(
        ft.Text("Generador de Contraseñas"),
        ft.Slider(min=8, max=32, divisions=24, label="{value}", on_change=lambda e: length_slider.value),
        ft.ElevatedButton("Generar", on_click=generate_button_clicked),
        ft.TextField(read_only=True, hint_text=password_text.value),
        
        
    )



ft.app(target=main)