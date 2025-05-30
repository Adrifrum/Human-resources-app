from dash import register_page
from layouts import NotFound404



register_page(
    __name__,
    path = '/notfound',
    title = '404 - Not Found'
)



layout = NotFound404(
    top_message = 'Page Not Found',
    bottom_message = 'Use the sidebar to navigate',
    src = '/assets/img/not_found_404.svg'
)
