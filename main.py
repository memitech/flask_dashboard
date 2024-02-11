from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    members = [
        {
        'name': 'Alexander Scholz',
        'phone': '012-345-678',
        'country': 'Denmark'
        },
        {
        'name': 'Marius Hoibraten',
        'phone': '123-456-789',
        'country': 'Norway'
        },
        {
        'name': 'Ekanit Panya',
        'phone': '234-567-890',
        'country': 'Thailand'
        },
    ]
    events = [

    ]
    return render_template(
        'index.html',
        members = members,
        events = events,
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

if __name__ == "__main__":
    app.run(debug=True)