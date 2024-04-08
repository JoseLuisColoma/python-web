import reflex as rx
from portfolio.components.link_button import link_button

def links() -> rx.Component:
    rx.vstack(
        link_button(),
        link_button(),
        link_button(),
        link_button(),
        link_button(),
        link_button(),
    )