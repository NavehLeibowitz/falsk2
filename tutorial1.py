from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<phrase>")
def home(phrase):
    return render_template("home.html", content=phrase)


"""
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
"""


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run()
