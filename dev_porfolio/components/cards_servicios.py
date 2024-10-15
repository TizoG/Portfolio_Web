import reflex as rx
from dev_porfolio.styles.colors import Color
from dev_porfolio.styles.fonts import Size


def cards_servicios(icon: str, title: str, text: str, color: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.icon(
                tag=icon,
                size=20,
                color=color
            ),
            rx.heading(
                title,
                font_size=Size.DEFAUL.value
            ),
            rx.text(
                text,
                font_size=Size.SMALL_MEDIUM.value
            ),
            margin=Size.SMALL_MEDIUM.value,
        ),
        border=f"{Color.BACKGROUND_CARD.value} 2px solid",
        border_radius=Size.SMALL_MEDIUM.value,
        max_height="155px",
        width="300px",  # Esto asegurará que el box ocupe todo el ancho disponible
        height="100%",  # Esto asegurará que el box ocupe todo el alto disponible
        align_items="center"
    )
