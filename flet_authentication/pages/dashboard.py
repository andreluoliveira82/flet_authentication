import flet as ft

from flet_authentication.utils.colors import *
from flet_authentication.utils.controls import *

# from flet_authentication.components.custom_fields import CustomTextField
from flet_authentication.components.custom_buttons import (
    CustomTextButton,
    CustomElevatedButton,
)


class Dashboard(ft.Container):
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
                                "Dashboard",
                                font_family="abeezee",
                                color=CUSTOM_TEXT_COLOR,
                                size=50,
                                weight=ft.FontWeight.BOLD,
                                expand=True,
                            ),
                            # button go to home_page
                            ft.Container(
                                # alignment=ft.alignment.center,
                                # height=BTN_HEIGHT,
                                # bgcolor=CUSTOM_BGCOLOR,
                                content=CustomTextButton("home page"),
                                on_click=lambda e: page.go("/"),
                            ),
                        ],
                    ),
                ),
                # container da direita
                ft.Container(
                    expand=3,
                    image_src="images/white-black-background-textures-1024.jpg",
                    image_opacity=0.3,
                    image_fit=ft.ImageFit.COVER,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Dashboard Seccion",
                                font_family="abeezee",
                                color=ft.colors.PURPLE,
                                size=50,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Divider(
                                color=ft.colors.PURPLE, height=0.5, thickness=0.2
                            ),
                            ft.Icon(
                                name=ft.icons.DASHBOARD_CUSTOMIZE,
                                size=100,
                                color=CUSTOM_TEXT_HEADER_COLOR,
                            ),
                            ft.Divider(
                                color=ft.colors.PURPLE, height=0.5, thickness=0.2
                            ),
                            ft.Container(
                                content=CustomElevatedButton(
                                    text="Home Page",
                                    bgcolor = 'green',
                                    on_click=lambda e: page.go("/"),
                                )
                            ),
                        ],
                    ),
                ),
            ]
        )
