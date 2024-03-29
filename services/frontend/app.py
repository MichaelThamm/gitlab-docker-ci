from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.config.update(
        TESTING=True,
        ENV='development'
    )
    app.run(debug=True, port=80)