import reflex as rx
from dev_porfolio.components.cards_servicios import cards_servicios
from dev_porfolio.styles.colors import TextColor
from dev_porfolio.styles.fonts import Size, Font


def menu_servicios() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.text(
                    "Menu de Servicios",
                    color=TextColor.ACCENT.value,
                    font_size=Size.MEDIUM.value,
                    font_family=Font.TERTIARY.value
                ),
                rx.text(
                    "¿Cómo puedo ayudar a su negocio?",
                    color=TextColor.PRIMARY.value,
                    font_size=Size.BIG.value,
                    margin_bottom=Size.BIG.value,
                    font_family=Font.TITLE.value
                ),
                rx.hstack(
                    cards_servicios(
                        "monitor",
                        "Sitios web y aplicaciones",
                        "Desarrollo de interfaces",
                        "#BB72E9"
                    ),
                    cards_servicios(
                        "server",
                        "API y Bases de Datos.",
                        "Creación de servicios del sistema",
                        "#EABD5F"
                    ),
                    cards_servicios(
                        "boxes",
                        "DevOps",
                        "Gestión e infraestructura de la aplicación.",
                        "#82BC4F"
                    )
                ),
                align_items="center"
            )
        ),
        margin_y=Size.VERY_BIG.value,
        max_width="1100px"
    )
