import reflex as rx
import dev_porfolio.styles.styles as styles
from dev_porfolio.views.header import header
from dev_porfolio.views.trabajo import my_trabajo
from dev_porfolio.views.menu_servicios import menu_servicios
from dev_porfolio.views.footer import footer


def index() -> rx.Component:
    return rx.center(
        rx.box(
            header(),
            my_trabajo(),
            menu_servicios(),
            footer()
        )
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Porfolio personal",
    description="Creacion de un portfolio."
)
