import reflex as rx
from dev_porfolio.components.link_button import link_button
from dev_porfolio.styles.fonts import Font, Size


def footer() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.text(
                    "Contacto",
                    color="#BB72E9",
                    font_size=Size.MEDIUM.value,
                    font_family=Font.TERTIARY.value
                ),
                rx.heading(
                    "¿Te gustó mi trabajo?",
                    font_size=Size.BIG.value,
                    font_family=Font.TITLE.value
                ),
                rx.text(
                    "¡Contáctame o sigue mis redes sociales!",
                    margin_bottom=Size.BIG.value,
                ),
                link_button("linkedin",
                            "Linkedin",
                            "arrow-up-right",
                            "[/urlinkendli]"
                            ),
                link_button("github",
                            "GitHub",
                            "arrow-up-right",
                            "[/url_github]"
                            ),
                link_button("mail",
                            "Email",
                            "arrow-up-right",
                            "[/url_email]"
                            ),
                align_items="center"
            )
        ),
        margin_y=Size.VERY_BIG.value
    )
