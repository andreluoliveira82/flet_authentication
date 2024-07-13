import flet as ft
import time

from flet_authentication.utils.colors import *
from flet_authentication.utils.controls import *
from flet_authentication.utils.validation import Validation
from flet_authentication.components.custom_fields import CustomTextField
from flet_authentication.components.custom_buttons import CustomTextButton
from flet_authentication.db import db_path
from flet_authentication.db.hash_passord import hash_password

from flet_authentication.db.crud import (
    connect_to_database,
    check_data_exists,
    insert_data,
)


class RegisterUser(ft.Container):
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

        # master container
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
                            
                            # btn register
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=BTN_HEIGHT,
                                bgcolor=CUSTOM_PRIMARY_COLOR,
                                content=ft.Text(
                                    "Registrar-me", size=16, color=CUSTOM_TEXT_COLOR
                                ),
                                on_click=self.register_user,
                            ),
                            # btns links
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Column(
                                    controls=[
                                        # button create account
                                        ft.Container(
                                            content=CustomTextButton(
                                                text="Já tem conta? Fazer Login"
                                            ),
                                            on_click=lambda e: page.go("/login"),
                                        ),
                                        # btn to go home_page
                                        ft.Container(
                                            content=CustomTextButton(text="Home Page"),
                                            on_click=lambda e: self.page.go("/"),
                                            visible=False
                                        ),
                                    ]
                                ),
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

    def register_user(self, e):
        """
        Registra um novo usuário no sistema.

        Args:
            e (_type_): Evento de trigger do register_user.
        """
        first_name_value = self.first_name.content.value
        last_name_value = self.last_name.content.value
        email_value = self.email.content.value
        password_value = self.password.content.value
        confirm_password_value = self.confirm_password.content.value

        if (
            first_name_value
            and last_name_value
            and email_value
            and password_value
            and confirm_password_value
        ):
            if confirm_password_value != password_value:
                self.display_error("As senhas digitadas não correspondem.")
                return False
            try:
                conn = connect_to_database(db_path=db_path)

                if not self.validation.is_valid_email(email=email_value):
                    self.display_error("Insira um email válido.", self.email)

                elif not check_data_exists(conn, "users", f"email='{email_value}'"):
                    insert_data(
                        conn=conn,
                        table_name="users",
                        values={
                            "first_name": first_name_value,
                            "last_name": last_name_value,
                            "email": email_value,
                            "password": hash_password(password_value),
                        },
                    )
                    self.show_splash_and_redirect(
                        self.page, error_field=self.error_field
                    )
                    return True
                else:
                    self.display_error("Este email já está em uso.", self.email)
                    return False
            except Exception as ex:
                self.display_error(
                    f"Ocorreu um erro ao conectar ao banco de dados: {ex}",
                    self.error_field,
                )
                return False
            finally:
                conn.close()
        else:
            self.display_error(
                "Todos os campos precisam ser preenchidos corretamente.",
                self.error_field,
            )
            return False

    def display_error(self, msg, field):
        """
        Exibe uma mensagem de erro no campo especificado.

        Args:
            msg (str): Mensagem de erro a ser exibida.
            field (ft.TextField): Campo onde a mensagem de erro será exibida.
        """
        field.border = self.error_border
        self.error_field.value = msg
        self.error_field.size = 14
        self.error_field.update()
        field.update()
        time.sleep(2)
        field.border = self.default_border
        self.error_field.size = 0
        self.error_field.update()
        field.update()

    def show_splash_and_redirect(self, page, error_field):
        """
        Exibe um splash de carregamento, mostra uma mensagem de sucesso e redireciona para a página de login.

        Args:
            page (ft.Page): A página atual.
            error_field (ft.TextField): Campo para exibir mensagens de erro.
        """
        splash = ft.ProgressBar()
        page.overlay.append(splash)
        error_field.value = "Seus dados foram cadastrados com sucesso!"
        error_field.color = CUSTOM_SUCCESS_TEXT_COLOR
        error_field.size = 14
        page.update()

        # Função que será chamada após o atraso
        def remove_splash_and_redirect():
            page.overlay.remove(splash)
            page.update()
            page.go("/login")

        # Atraso de 2 segundos
        time.sleep(2)
        remove_splash_and_redirect()
