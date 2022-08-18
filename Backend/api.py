from flask import Flask, render_template

api = Flask(__name__)


@api.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    api.config.update(
        TESTING=True,
        ENV='development'
    )
    api.run(debug=True)