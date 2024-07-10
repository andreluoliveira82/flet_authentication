import flet as ft
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
        page.fonts = {"abeezee": "fonts/ABeeZee-Regular.ttf"}
        # page.window.maximized=True
        page.update()

    page.on_route_change = route_change

    # Definindo a rota inicial como "/login"
    page.go("/login")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
