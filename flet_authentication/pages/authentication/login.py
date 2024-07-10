import flet as ft

from flet_authentication.utils.colors import *
from flet_authentication.utils.controls import *
from flet_authentication.components.fields import CustomTextField


class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        self.email = ft.Container(
            content=CustomTextField(
                label="Email",
                color=CUSTOM_TEXT_COLOR,
                bgcolor=CUSTOM_BGCOLOR,
                border=ft.border.all(width=1, color=CUSTOM_BORDER_COLOR),
                autofocus=True,
            )
        )

        self.password = ft.Container(
            content=CustomTextField(
                label="Password",
                color=CUSTOM_TEXT_COLOR,
                bgcolor=CUSTOM_BGCOLOR,
                border=ft.border.all(width=1, color=CUSTOM_BORDER_COLOR),
                autofocus=False,
                password=True,
                can_reveal_password=True,
            )
        )

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
                                color=CUSTOM_TEXT_COLOR,
                                font_family="abeezee",
                                size=20,
                                weight=ft.FontWeight.NORMAL,
                                # expand=True,
                            ),
                            ft.Divider(
                                color=CUSTOM_BORDER_COLOR, height=0.8, thickness=1
                            ),
                            # add the email and password fields
                            self.email,
                            self.password,
                            # add the buttons
                            # button Login
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=BTN_HEIGHT,
                                bgcolor=CUSTOM_PRIMARY_COLOR,
                                content=ft.Text(
                                    "Login", size=16, color=CUSTOM_TEXT_COLOR
                                ),
                                on_click=lambda e: page.go("/dashboard"),
                            ),
                            # button create account
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=BTN_HEIGHT,
                                bgcolor=CUSTOM_BGCOLOR,
                                content=ft.Text(
                                    "Create Account",
                                    size=12,
                                    color=ft.colors.BLUE,
                                    style=ft.TextStyle.baseline,
                                ),
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
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(
                                name=ft.icons.LOCK_PERSON_ROUNDED,
                                size=200,
                                color=CUSTOM_TEXT_HEADER_COLOR,
                            ),
                            ft.Text(
                                "Login Seccion",
                                color=ft.colors.BLACK,
                                size=20,
                                weight=ft.FontWeight.NORMAL,
                            ),
                        ],
                    ),
                ),
            ]
        )
