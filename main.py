import flet as ft

from flet_authentication.db.db import create_database
from flet_authentication.router import views_handler


def main(page: ft.Page):

    def route_change(event):
        route = event.route
        page.views.clear()

        views = views_handler(page)

        if route in views:
            page.views.append(views[route])
        else:
            page.views.append(
                ft.View(
                    route=route,
                    controls=[ft.Text("Page not found", color="red")],
                )
            )
        page.fonts = {"abeezee": "fonts/ABeeZee-Regular"}
        # page.window.maximized=True
        page.update()

    page.on_route_change = route_change

    # Definindo a rota inicial como "/login"
    page.go("/login")


if __name__ == "__main__":
    # Cria o banco de dados e a tabela users, se ainda não existir
    create_database()
    ft.app(target=main, assets_dir="assets")
