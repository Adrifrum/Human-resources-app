from typing import Optional
import uuid
import dash_bootstrap_components as dbc


from dash import html
from dash.development.base_component import Component

logo_adc = "https://upload.wikimedia.org/wikipedia/commons/a/a2/OECD_logo.svg"


class Navbar(html.Nav):
    def __init__(
            self,
            id: Optional[str] = None
        ):
        """Navbar components.

        Parameters
        ----------
        title : str | Dash Component
            Text displayed inside the navbar.
        children : Dash Component, optional
            Content in the right of the navbar.
        id : str, optional
            Component's ID.

        Components IDs
        --------------
        {id}--title
            Navbar title.
        {id}--children
            Content in the right of the navbar.
        
        """

        id = id or str(uuid.uuid4())

        super().__init__(
            className = 'home-content shade7',
            children = [
                html.I(
                    className = 'fas fa-bars',
                    id = 'open-drawer'
                ),
                html.Span(
                    children = [
                            html.Span(
                                className = 'text',
                                children = [html.A(
                                # Use row and col to control vertical alignment of logo / brand
                                dbc.Row(
                                [
                                    dbc.Col(html.Img(src=logo_adc, height="40px"), width="auto"),
                                ],
                                align="center",
                                ),
                                href="/",
                                )],
                            id = f'{id}--children'
                        )
                    ],
                    style = {
                        'width': '100%',
                        'display': 'flex',
                        'justify-content': 'space-between'
                    }
                )
            ]
        )
