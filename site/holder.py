from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("/main.html")

@app.route("/view")
def viewer():
    return render_template("/viewer.html")

app.run()