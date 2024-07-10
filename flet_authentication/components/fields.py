import flet as ft

from flet_authentication.utils.colors import *

class CustomTextField(ft.TextField):
    def __init__(
        self,
        label,
        autofocus=False,
        icon=None,
        password=False,
        border=ft.InputBorder.NONE,
        can_reveal_password=False,
        error_text=None,
        input_filter=None,
        bgcolor = CUSTOM_BGCOLOR,
        **kwargs
    ):

        super().__init__(
            label=label,
            autofocus=autofocus,
            icon=icon,
            password=password,
            border=border,
            border_color=CUSTOM_BORDER_COLOR,
            can_reveal_password=can_reveal_password,
            error_text=error_text,
            input_filter=input_filter,
            content_padding=ft.padding.only(top=0, bottom=0, left=20, right=20),
            hint_style=ft.TextStyle(size=14, color=CUSTOM_TEXT_COLOR),
            focused_color=CUSTOM_TEXT_COLOR,
            bgcolor=bgcolor,
            **kwargs
        )
