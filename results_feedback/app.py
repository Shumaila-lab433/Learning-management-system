
from flask import Flask, render_template
from config import SECRET_KEY
from db import create_tables

from routes.teacher import teacher
from routes.student import student

app = Flask(__name__)
app.secret_key = SECRET_KEY

create_tables()

app.register_blueprint(teacher)
app.register_blueprint(student)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
