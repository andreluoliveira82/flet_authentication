import flet as ft


class CustomTextButton(ft.Text):
    def __init__(
        self,
        text,
        style=ft.TextStyle(color=ft.colors.BLUE, size=12),
        **kwargs,
    ):
        super().__init__(text, **kwargs)
        self.style = style

        self.content = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text(
                text,
                style=self.style,
            ),
        )



class CustomElevatedButton(ft.ElevatedButton):
    def __init__(
        self,
        text,
        on_click=None,
        color="white",
        bgcolor="blue",
        border_radius=8,
        width=200,
        height=50,
        **kwargs,
    ):
        """
        Inicializa um CustomElevatedButton com estilos e comportamento personalizados.

        Args:
            text (str): Texto a ser exibido no botão.
            on_click (callable, optional): Função a ser chamada quando o botão for clicado. Padrão é None.
            color (str, optional): Cor do texto do botão. Padrão é branco.
            bgcolor (str, optional): Cor de fundo do botão. Padrão é azul.
            border_radius (int, optional): Raio da borda do botão. Padrão é 8.
            width (int, optional): Largura do botão. Padrão é 200.
            height (int, optional): Altura do botão. Padrão é 50.
            **kwargs: Argumentos adicionais que podem ser passados para o ElevatedButton.
        """
        super().__init__(
            text=text,
            on_click=on_click,
            width=width,
            height=height,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=border_radius),
                color=color,
                bgcolor=bgcolor,
                elevation=5,
            ),
            **kwargs,
        )
