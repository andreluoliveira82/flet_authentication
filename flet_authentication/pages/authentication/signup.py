import flet as ft
import time

from flet_authentication.utils.colors import *
from flet_authentication.utils.controls import *
from flet_authentication.utils.validation import Validation
from flet_authentication.components.fields import CustomTextField
from flet_authentication.db import db_path

from flet_authentication.db.crud import (
    connect_to_database,
    check_data_exists,
    insert_data,
)


class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        # aqui vamos validar alguns campos utilizando nossa classe Validation
        self.validation = Validation()
        self.default_border = ft.border.all(width=1, color=CUSTOM_BORDER_COLOR)
        self.error_border = ft.border.all(color="red", width=1)
        self.error_field = ft.Text(value="", color="red", size=0)

        self.first_name = ft.Container(
            content=CustomTextField(
                label="Nome",
                color=CUSTOM_TEXT_COLOR,
                bgcolor=CUSTOM_BGCOLOR,
                border=ft.border.all(width=1, color=CUSTOM_BORDER_COLOR),
                autofocus=True,
            )
        )
        self.last_name = ft.Container(
            content=CustomTextField(
                label="Sobrenome",
                color=CUSTOM_TEXT_COLOR,
                bgcolor=CUSTOM_BGCOLOR,
                border=ft.border.all(width=1, color=CUSTOM_BORDER_COLOR),
                autofocus=True,
            )
        )

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
                label="Senha",
                color=CUSTOM_TEXT_COLOR,
                bgcolor=CUSTOM_BGCOLOR,
                border=ft.border.all(width=1, color=CUSTOM_BORDER_COLOR),
                autofocus=False,
                password=True,
                can_reveal_password=True,
            )
        )

        self.confirm_password = ft.Container(
            content=CustomTextField(
                label="Confirme a senha",
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
                                "Registre-se",
                                color=CUSTOM_TEXT_COLOR,
                                font_family="abeezee",
                                size=20,
                                weight=ft.FontWeight.NORMAL,
                                # expand=True,
                            ),
                            ft.Divider(
                                color=CUSTOM_BORDER_COLOR, height=0.8, thickness=1
                            ),
                            # add the fields
                            self.error_field,  # field to show error message
                            self.first_name,
                            self.last_name,
                            self.email,
                            self.password,
                            self.confirm_password,
                            # button Login
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=BTN_HEIGHT,
                                bgcolor=CUSTOM_PRIMARY_COLOR,
                                content=ft.Text(
                                    "Registrar-me", size=16, color=CUSTOM_TEXT_COLOR
                                ),
                                on_click=self.signup,
                            ),
                            # button create account
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=BTN_HEIGHT,
                                bgcolor=CUSTOM_BGCOLOR,
                                content=ft.Text(
                                    "Login",
                                    size=12,
                                    color=ft.colors.BLUE,
                                    style=ft.TextStyle.baseline,
                                ),
                                on_click=lambda e: page.go("/login"),
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
                                "Register Seccion",
                                color=ft.colors.BLACK,
                                size=20,
                                weight=ft.FontWeight.NORMAL,
                            ),
                        ],
                    ),
                ),
            ]
        )

    def signup(self, e):
        # getting the values ​​filled in the fields
        first_name_value = self.first_name.content.value
        last_name_value = self.last_name.content.value
        email_value = self.email.content.value
        password_value = self.password.content.value
        confirm_password_value = self.confirm_password.content.value

        # check that no fields is empty
        if (
            first_name_value
            and last_name_value
            and email_value
            and password_value
            and confirm_password_value
        ):
            # self.page.go("/dashboard")

            # establishes an connection to the database
            conn = connect_to_database(db_path=db_path)

            # chech is valid email
            if not self.validation.is_valid_email(email=email_value):
                # in this case, the email is'nt valid
                msg = "Insira um email válido."
                self.email.border = self.error_border
                self.error_field.value = msg
                self.error_field.size = 14
                self.error_field.update()
                self.email.update()
                time.sleep(2)  # Espera de forma não bloqueante
                self.email.border = self.default_border
                self.error_field.size = 0
                self.error_field.update()
                self.email.update()

            # check if email already exists in database. If it doesn't exist, we will create the account
            elif not check_data_exists(conn, "users", f"email='{email_value}'"):
                print("This is our signup")
                # insert data into table in database
                insert_data(
                    conn=conn,
                    table_name="users",
                    values={
                        "first_name": first_name_value,
                        "last_name": last_name_value,
                        "email": email_value,
                        "password": password_value,
                    },
                )
                # # exibe um splash e uma mensagem de sucesso
                # self.page.splash = ft.ProgressBar()
                # self.error_field.value = "Seus dados foram cadastrado com sucesso!"
                # self.error_field.color = CUSTOM_SUCCESS_TEXT_COLOR
                # self.error_field.size = 14
                # self.page.update()
                # time.sleep(2)  # Espera de forma não bloqueante
                # self.page.splash = None
                # self.page.update()
                # self.page.go("/login")

                self.show_splash_and_redirect(self.page,error_field=self.error_field)
                
            else:
                # In this case the email is valid, but is already being used
                msg = "Este email já está em uso."
                self.email.border = self.error_border
                self.error_field.value = msg
                self.error_field.size = 14
                self.error_field.update()
                self.email.update()
                time.sleep(2)
                self.email.border = self.default_border
                self.error_field.size = 0
                self.error_field.update()
                self.email.update()

        else:
            # in case any mandatory field is empty
            # display an error message in the error_field field
            msg = "Todos os campos precisam ser preenchidos corretamente."
            self.error_field.value = msg
            self.error_field.size = 14
            self.error_field.update()
            time.sleep(2)
            self.error_field.size = 0
            self.error_field.update()

    def show_splash_and_redirect(self, page, error_field):
        page.splash = ft.ProgressBar()
        error_field.value = "Seus dados foram cadastrado com sucesso!"
        error_field.color = CUSTOM_SUCCESS_TEXT_COLOR
        error_field.size = 14
        page.update()

        # Função que será chamada após o atraso
        def remove_splash_and_redirect():
            page.splash = None
            page.update()
            page.go("/login")
            
        # Atraso de 2 segundos
        time.sleep(2)
        remove_splash_and_redirect()
