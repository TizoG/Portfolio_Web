import reflex as rx
from dev_porfolio.components.link_button_tag import link_button_tag


def tag() -> rx.Component:
    return rx.hstack(
        link_button_tag(
            "github",
            "GitHub"
        ),
        link_button_tag(
            "code-xml",
            "HTML"
        ),
        link_button_tag(
            "code-xml",
            "CSS"
        ),
        link_button_tag(
            "file-json",
            "Javascript"
        ),
        link_button_tag(
            "code-xml",
            "React"
        ),
        link_button_tag(
            "hexagon",
            "Node.js"
        ),
    )
