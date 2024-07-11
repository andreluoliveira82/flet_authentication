import flet as ft
import time

from flet_authentication.utils.colors import *
from flet_authentication.utils.controls import *
from flet_authentication.utils.validation import Validation
from flet_authentication.components.fields import CustomTextField
from flet_authentication.db import db_path
from flet_authentication.db.hash_passord import hash_password

from flet_authentication.db.crud import (
    connect_to_database,
    check_data_exists,
    insert_data,
    get_data,
)


class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        # aqui vamos validar alguns campos utilizando nossa classe Validation
        self.validation = Validation()
        self.default_border = ft.border.all(width=1, color=CUSTOM_BORDER_COLOR)
        self.error_border = ft.border.all(color="red", width=1)
        self.error_field = ft.Text(value="", color="red", size=0)

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
                            # add the fields here
                            self.error_field,
                            self.email,
                            self.password,
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=BTN_HEIGHT,
                                bgcolor=CUSTOM_PRIMARY_COLOR,
                                content=ft.Text(
                                    "Login", size=16, color=CUSTOM_TEXT_COLOR
                                ),
                                
                                on_click=self.login, # lambda e: page.go("/dashboard")
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

    # method for login validation
    def login(self, e):
        """valida o login, verificando se o email informado existe no bando de dados, na tabela users.
        Se o email existir, verifica se a senha informada é a mesma que está no banco.
        Se a senha for correta, o usuário é redirecionado para a página Home.

        Args:
            e (_type_): _description_
        """
        email_value = self.email.content.value
        password_value = hash_password(self.password.content.value)
        
        if email_value and password_value:
            # open connection with database
            conn = connect_to_database(db_path)

            # check if exists this email and load data, case true
            if check_data_exists(conn, "users", f"email='{email_value}'"):
                # load data from database
                get_user = get_data(conn, "users", f"email='{email_value}'")
                is_email_match = get_user[0]["email"] == email_value
                is_password_match = get_user[0]["password"] == password_value

                if is_email_match and is_password_match:
                    self.page.splash = ft.ProgressBar()
                    self.page.update()
                    time.sleep(2)
                    self.page.splash = None
                    self.page.go("/") # home
                else:
                    msg = "Email ou Senha estão incorretos"
                    self.email.border = self.error_border
                    self.error_field.value = msg
                    self.error_field.size = 14
                    self.password.update()
                    self.email.update()
                    self.error_field.update()

                    time.sleep(2)
                    self.email.border = self.default_border
                    self.password.border = self.default_border
                    self.error_field.size = 0
                    self.password.update()
                    self.email.update()
                    self.error_field.update()
