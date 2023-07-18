import dash
import dash_player
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Iframe(src="https://www.youtube.com/embed/DHUnz4dyb54?controls=0&showinfo=0&rel=0&modestbranding=1&autoplay=1",
                    style={"width": "100%", "height": "100%"})#,
        html.Div(style={"width": "100%", "height": "100%", "position": "absolute", "top": "0", "left": "0"})
    ], style={"width": "60%", "height": "360px", "position": "relative", "margin": "auto"}),
])

if __name__ == "__main__":
    app.run_server(debug=True)