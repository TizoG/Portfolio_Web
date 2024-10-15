import reflex as rx
from dev_porfolio.styles.colors import TextColor
from dev_porfolio.styles.fonts import Size, Font
from dev_porfolio.components.tag import tag


def header() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.avatar(
                    fallback="RX",  # Puedes introducir aqui tu imagen
                    border=f"0.25em solid {TextColor.ACCENT.value},",
                    size="8",
                    radius="full",
                    padding=Size.SMALL.value,
                    margin_top=Size.VERY_BIG.value,
                    margin_bottom=Size.MEDIUM.value
                ),
                rx.text(
                    "¡Hola Mundo! Mi nombre es ",
                    rx.text.span("[Tu nombre]", color=TextColor.ACCENT.value),
                    "y soy",
                    font_family=Font.TERTIARY.value,
                    font_size=Size.MEDIUM.value,
                    color=TextColor.SECUNDARY.value,
                    margin_bottom=Size.SMALL.value
                ),
                rx.heading(
                    "Desarrollador Fullstack",
                    font_size=Size.VERY_BIG.value,
                    margin_bottom=Size.SMALL.value,
                    font_family=Font.TITLE.value
                ),
                rx.text(
                    "Transformo necesidades en aplicaciones reales, envolventes y funcionales. Desarrolllo sistemas a través de mi pasión por la tecnología, contribuyendo con soluciones innovadoras y eficaces para desafíos complejos.",
                    font_size=Size.SMALL_MEDIUM.value,
                    margin_bottom=Size.SMALL.value,
                    color=TextColor.TERTIARY.value
                ),
                tag(),
                rx.icon(
                    tag="chevrons-down",
                    margin_top=Size.BIG_BIG.value,
                    size=40,
                    color=TextColor.TERTIARY.value
                ),
                align_items="center",
                justify_content="center"
            ),
            max_width="700px",
            justify="center"
        ),
        margin_y=Size.BIG_BIG.value,
        display="flex",
        justify_content="center"

    )
