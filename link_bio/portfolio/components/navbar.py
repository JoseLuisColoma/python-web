import reflex as rx


def navbar():
    return rx.hstack(
        rx.hstack(
            rx.image(src="/jocodev-02.png", width="8rem", vertical_align="center", margin_left="10px"),
            rx.heading("Portfolio", font_size="2em", margin_left="50x"),
        ),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Menu"),
                margin_right='20px',
            ),
            rx.menu.content(
                rx.menu.item("Proyectos"),
                rx.menu.separator(),
                rx.menu.item("Ejercicios Programacion"),
                rx.menu.separator(),
                rx.menu.item("Biblioteca"),
                rx.menu.separator(),
                rx.menu.item("Sobre mí"),
                rx.menu.separator(),
                rx.menu.item("Contacto"),
            ),
        ),
        position="fixed",
        top="0px",
        background_color="lightgray",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
    )
    
