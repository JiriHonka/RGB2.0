from flask import Flask, render_template, request

app = Flask(__name__)

history = []
available_colors = [
    'red', 'green', 'blue', 'lime', 'black', 'cyan', 'yellow', 'magenta', 'white', 'gray', 'orange', 'pink', 'purple', 'brown'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    global history

    if request.method == 'POST' and request.form.get('clear'):
        history = []
        color1, color2, color3 = 'red', 'green', 'blue'
    else:
        color1 = request.form.get('color1', 'red')
        color2 = request.form.get('color2', 'green')
        color3 = request.form.get('color3', 'blue')

        if request.method == 'POST':
            history.insert(0, (color1, color2, color3))

    return render_template('index.html', color1=color1, color2=color2, color3=color3, history=history, available_colors=available_colors)

if __name__ == '__main__':
    app.run(debug=True)