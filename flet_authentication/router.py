import flet as ft

from .pages.authentication.login import Login
from .pages.authentication.signup import SignUp
from .pages.dashboard import Dashboard

from .utils.colors import *


def views_handler(page):
    # print("passei aqui no views_handler")
    return {
        "/login": ft.View(
            "/login",
            bgcolor=CUSTOM_BGCOLOR,
            padding=ft.padding.all(0),
            controls=[Login(page)],
        ),
        "/signup": ft.View(
            "/signup",
            bgcolor=CUSTOM_BGCOLOR,
            padding=ft.padding.all(0),
            controls=[SignUp(page)],
        ),
        "/dashboard": ft.View(
            "/dashboard",
            bgcolor=CUSTOM_BGCOLOR,
            padding=ft.padding.all(0),
            controls=[Dashboard(page)],
        ),
    }
