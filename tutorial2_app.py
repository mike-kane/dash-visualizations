import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']},
    children=[
        html.H1(
            children='Hello Dash!',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(children='Dash: A web application framework for Python', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        dcc.Graph(
            id='example_graph_2',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [1, 2, 5], 'type': 'bar', 'name': 'Montreal'},
                    {'x': [1, 2, 3], 'y': [10, -2, -15], 'type': 'bar', 'name': 'Ocala'}
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']

                    }
                }
            }
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)
