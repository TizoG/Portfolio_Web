import reflex as rx
from dev_porfolio.styles.colors import Color
from dev_porfolio.styles.fonts import Size


def link_button_tag(image: str, text: str) -> rx.Component:
    return rx.button(
        rx.icon(tag=image),
        text,
        bg=Color.ACCENT.value,
        border_radius=Size.VERY_BIG.value
    )
