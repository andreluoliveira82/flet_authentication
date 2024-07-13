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
    get_data,
)


class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        # aqui vamos validar alguns campos utilizando nossa classe Validation
        self.validation = Validation()
        self.default_border = ft.border.all(width=1, color=CUSTOM_BORDER_COLOR)
        self.error_border = ft.border.all(color="red", width=2)
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
                                on_click=self.login,  # lambda e: page.go("/dashboard")
                            ),
                            # button create account
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=BTN_HEIGHT,
                                bgcolor=CUSTOM_BGCOLOR,
                                content=CustomTextButton(text="Create Account"),
                                on_click=lambda e: page.go("/register_user"),
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
    def login(self, e) -> bool:
        """
        Valida o login verificando se o email informado existe no banco de dados, na tabela 'users'.
        Se o email existir, verifica se a senha informada é a mesma que está no banco.
        Se a senha for correta, o usuário é redirecionado para a página Home.

        Args:
            e (_type_): Evento de trigger do login.

        Returns:
            bool: True se o login for válido, False caso contrário.
        """
        email_value = self.email.content.value
        password_value = hash_password(self.password.content.value)

        if email_value and password_value:
            
            if not self.validation.is_valid_email(email_value):
                self.error_message("Email inválido. Tente novamente.")
                return False
            try:
                conn = connect_to_database(db_path)
                if check_data_exists(conn, "users", f"email='{email_value}'"):
                    user_data = get_data(conn, "users", f"email='{email_value}'")[0]
                    if self.validate_user(user_data, email_value, password_value):
                        self.redirect_to_home()
                        return True
                    else:
                        self.error_message(
                            "Senha incorreta. Verifique e tente novamente"
                        )
                        return False
                else:
                    self.error_message(
                        "Email não cadastrado. Você pode realizar o cadastro do seu email e tentar novamente."
                    )
                    return False
            except Exception as ex:
                self.error_message(
                    f"Ocorreu um erro ao conectar ao banco de dados: {ex}"
                )
                return False
            finally:
                conn.close()
        else:
            self.error_message("Informe seu email e senha corretamente")
            return False

    def validate_user(self, user_data, email, password) -> bool:
        """
        Verifica se o email e a senha correspondem aos dados do usuário.

        Args:
            user_data (dict): Dados do usuário retornados do banco de dados.
            email (str): Email informado.
            password (str): Senha informada (já hashada).

        Returns:
            bool: True se os dados forem válidos, False caso contrário.
        """
        return user_data["email"] == email and user_data["password"] == password

    def redirect_to_home(self):
        """
        Redireciona o usuário para a página Home.
        """
        progress_bar = ft.ProgressBar()
        self.page.overlay.append(progress_bar)
        self.page.update()
        time.sleep(2)
        self.page.overlay.remove(progress_bar)
        self.page.update()
        self.page.go("/")  # home

    def error_message(self, msg):
        """
        Exibe uma mensagem de erro na interface do usuário.

        Args:
            msg (str): Mensagem de erro a ser exibida.
        """
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
