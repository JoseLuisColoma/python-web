
import reflex as rx
from portfolio.components.navbar import navbar
from portfolio.views.header.header import header
from portfolio.views.links.links import links
from portfolio.views.footer.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )


app = rx.App()
app.add_page(index)
