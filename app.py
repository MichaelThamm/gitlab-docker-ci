import sqlite3
import emailer
import cgi
from flask import Flask, render_template, request

# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
# https://www.w3schools.com/w3css/w3css_templates.asp
# https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_parallax&stacked=h

app = Flask(__name__)


@app.route('/')
def index():
    # Key value pairs from url after ?
    content = updatePage()

    # If a URL request has ? followed by key value pairs and there is a method key it was generated with the form's hidden id
    if request.args.get("method") == "emailer.py":
        emailer.run(request.args)

    # Run the index HTML code with contents from the database
    return render_template('index.html', posts=content)


def updatePage():
    # TODO Add the email functionality here
    # Open the database connection
    conn = get_db_connection()
    # Select all entries from posts table and fetch all rows of the query result
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return posts


def get_db_connection():
    conn = sqlite3.connect('database.db')
    # set the row_factory attribute to sqlite3.Row for name-based access to columns
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == "__main__":
    app.config.update(
        TESTING=True,
        ENV='development'
    )
    app.run(debug=True)