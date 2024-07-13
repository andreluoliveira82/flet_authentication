import flet as ft

from .pages.authentication.login import Login
from .pages.authentication.register import RegisterUser
from .pages.dashboard import Dashboard
from .pages.home_page import HomePage

from .utils.colors import *


def views_handler(page):
    return {
        
        "/": ft.View(
            # home
            "/",
            bgcolor=CUSTOM_BGCOLOR,
            padding=ft.padding.all(0),
            controls=[HomePage(page)],
        ),
        "/login": ft.View(
            "/login",
            bgcolor=CUSTOM_BGCOLOR,
            padding=ft.padding.all(0),
            controls=[Login(page)],
        ),
        "/register_user": ft.View(
            "/register_user",
            bgcolor=CUSTOM_BGCOLOR,
            padding=ft.padding.all(0),
            controls=[RegisterUser(page)],
        ),
        "/dashboard": ft.View(
            "/dashboard",
            bgcolor=CUSTOM_BGCOLOR,
            padding=ft.padding.all(0),
            controls=[Dashboard(page)],
        ),
    }
