from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Matt'}
    return render_template('index.html', title='Home', user=user)


if __name__ == '__main__':
    app.run(debug=True)
