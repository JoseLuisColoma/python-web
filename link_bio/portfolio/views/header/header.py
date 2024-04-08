import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.avatar(src="../../../assets/Jose CV.png"),
            rx.text("@jocodev"),
            rx.text("HOLA, MI NOMBRE ES JOSE LUIS"),
            rx.text("Soy desarrollador web full stack"),
        )
    )