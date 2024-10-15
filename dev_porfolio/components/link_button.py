import reflex as rx
from dev_porfolio.styles.colors import Color, TextColor


def link_button(image: str, text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.flex(
                rx.hstack(
                    rx.icon(
                        tag=image,
                        color=TextColor.SECUNDARY.value,
                    ),
                    rx.text(
                        text,
                        color=TextColor.SECUNDARY.value
                    ),
                    flex="1",
                ),
                # rx.separator(),
                rx.hstack(
                    rx.icon(
                        tag=icon,
                        color="#3996DB",
                    ),
                ),
                align_items="center",
                justify="space-between",
                width="100%",
            ),
            background=Color.ACCENT.value,
            border="transparent solid 1px",
            height="68px",
            width="400px",
            _hover={  # Efectos al pasar el ratón sobre el botón
                "border_color": "#3996DB",  # Cambia el color del borde
                "cursor": "pointer",  # Cambia el cursor
                "& > div > div > svg": {  # Cambia el color de los íconos
                    "color": "#3996DB"  # Nuevo color para los íconos
                },
            },
        ),
        href=url
    )
