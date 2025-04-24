from dash import Dash, page_container
import dash_bootstrap_components as dbc

import themes
from components import (
    Dashboard,
    Drawer,
    DrawerSingleItem,
    DrawerMultiItem,
    DrawerSubItem,
    DrawerFooter,
    Navbar
)

server = Flask(__name__)

app = Dash(
    server=server,
    name = __name__,
    title = 'Dash Charlotte',
    use_pages = True,
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        themes.BOOTSTRAP,
        themes.BOXICONS,
        themes.BUTTONS,
        themes.FONTAWESOME,
        themes.CHARLOTTE_LIGHT
    ]
)

nav_links = [
    DrawerSingleItem(
        name='Dashboard',
        icon='bx bx-line-chart',
        href='/'
    ),
    DrawerSingleItem(
        name='About the project',
        icon='bx bx-help-circle',
        href='/aboutus'
    )
]

LOGO_ICON = 'fas fa-rocket'
LOGO_IMG = "https://upload.wikimedia.org/wikipedia/commons/a/a2/OECD_logo.svg"


app.layout = Dashboard(
    children= page_container,
    navbar=Navbar(
    ),
    drawer=Drawer(
        menu=nav_links,
        logo_name='Démo scraping',
        logo_icon=LOGO_ICON,
    )
)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
