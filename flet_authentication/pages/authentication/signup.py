import flet as ft

class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.content = ft.Column(
            controls=[
                ft.Text("hello Sign Up section!", color='pink'),
                ft.ElevatedButton("Login", icon=ft.icons.LOGIN, on_click=lambda e: page.go("/login"))
            ]
        ) 
        