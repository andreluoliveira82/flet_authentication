import flet as ft
import os

from flet_authentication.utils.colors import *


class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        self.content = ft.Row(
            controls=[
                # container da esquerda
                ft.Container(
                    expand=2,
                    padding=ft.padding.all(40),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Welcome Back",
                                color=CUSTOM_TEXT_HEADER_COLOR,
                                size=40,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.ElevatedButton(
                                "Sign Up",
                                icon=ft.icons.LOGOUT,
                                on_click=lambda e: page.go("/signup"),
                            ),
                        ],
                    ),
                ),
                # container da direita
                ft.Container(
                    expand=3,
                    image_src="images/white-black-background-textures-1024.jpg",
                    image_fit=ft.ImageFit.COVER,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Container da Direita",
                                color=CUSTOM_TEXT_HEADER_COLOR,
                                size=40,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                ),
            ]
        )
