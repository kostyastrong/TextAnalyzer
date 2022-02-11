from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("/main.html")

@app.route("/view")
def viewer():
    name = request.args["name"]
    begin = request.args["begin"]
    print(name, begin)
    return render_template("/viewer.html")



@app.errorhandler(404)
def page_not_found(e):
    return render_template('/404.html'), 404

a = 5
app.run(debug=True, port=5000)