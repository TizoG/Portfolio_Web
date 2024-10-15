import reflex as rx
from dev_porfolio.styles.colors import TextColor
from dev_porfolio.styles.fonts import Size, Font
from dev_porfolio.components.link_cards import link_cards


def my_trabajo() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.text(
                    "Mi trabajo",
                    color=TextColor.ACCENT.value,
                    font_size=Size.MEDIUM.value,
                    font_family=Font.TERTIARY.value
                ),
                rx.text(
                    "Proyectos destacados.",
                    color=TextColor.PRIMARY.value,
                    font_size=Size.BIG.value,
                    font_family=Font.TITLE.value
                ),
                rx.flex(
                    # Cambia los link de las imagenes por las tuyas, los titulos y los subtitulos
                    link_cards(
                        "[Thumbnail_Project-01.png]",
                        "imagen del proyecto",
                        "Travelgram",
                        "Red social donde las personas muestran los registros de sus viajes por el mundo."
                    ),
                    link_cards(
                        "[Thumbnail_Project-02.png]",
                        "imagen del proyecto",
                        "Noticias de Tecnología",
                        "Página principal de un portal de noticias sobre el área de tecnología."
                    ),
                    link_cards(
                        "[Thumbnail_Project-03.png]",
                        "imagen del proyecto",
                        "Página de recetas",
                        "Página con el paso a paso de una receta para cupcakes."
                    ),
                    link_cards(
                        "/dev_porfolio/assets/Thumbnail_Project-04.png",
                        "imagen del proyecto",
                        "Cantando",
                        "Página de destino completa y responsiva de una aplicación de karaoke."
                    ),
                    link_cards(
                        "/dev_porfolio/assets/Thumbnail_Project-05.png",
                        "imagen del proyecto",
                        "Reembolso",
                        "Un sistema para solicitar y hacer seguimiento de reembolsos."
                    ),
                    link_cards(
                        "/dev_porfolio/assets/Thumbnail_Project-06.png",
                        "imagen del proyecto",
                        "Página de turismo.",
                        "Página con la información principal para quienes desean viajar a Busan."
                    ),
                    flex_wrap="wrap",
                    gap=Size.MEDIUM.value,
                    justify="between",
                    padding_y=Size.VERY_BIG.value,

                ),
                align_items="center",

            ),
        ),
        max_width="1100px"
    )
