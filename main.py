from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


year = datetime.now().year


@app.route("/")
def home():
    return render_template(
        "index.html",
        year=year
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        year=year
    )


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template(
        "contact",
        year=year
    )


if __name__ == "__main__":
    app.run()