import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
            rx.avatar(name="JocoDev", size="5"),
            rx.text("@jocodev"),
            rx.text("HOLA, MI NOMBRE ES JOSE LUIS"),
            rx.text("Soy desarrollador web full stack"),
    )
