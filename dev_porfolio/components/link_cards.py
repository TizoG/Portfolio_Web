import reflex as rx
from dev_porfolio.styles.colors import Color
from dev_porfolio.styles.fonts import Size
from dev_porfolio.styles.colors import TextColor


def link_cards(image: str, atrb: str, title: str, parrafo: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(
                src=image,
                alt=atrb,
                height="156px",
                width="306px"
            ),
            rx.heading(
                title
            ),
            rx.text(
                parrafo,
                font_size=Size.SMALL_MEDIUM.value
            ),
        ),
        max_width="330px",
        max_height="280px",
        background=Color.BACKGROUND_CARD.value,
        border_radius=Size.SMALL.value,
        padding=Size.SMALL_MEDIUM.value,
        border="transparent solid 1px",
        transition="all 0.3s ease",
        _hover={
            "border": f"{TextColor.TERTIARY.value} solid 1px",
            "cursor": "pointer"

        }
    )
