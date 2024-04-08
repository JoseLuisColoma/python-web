import reflex as rx
from portfolio.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("Proyectos"),
        link_button("Ejercicios de programación"),
        link_button("Sobre mi"),
        link_button("Contacto")
    )
