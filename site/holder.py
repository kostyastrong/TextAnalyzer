from flask import Flask, render_template, request

from nbformat import current_nbformat

app = Flask(__name__)

def get_book(path):
    with open(path, mode='r') as f:
        contents = f.read()
    return contents

@app.route('/')
def main():
    return render_template("/main.html")

@app.route('/ajax')
def ajax():
    current = request.cookies.get("current")
    content = "Hello my dear friend fuck you"
    if(current == '1'):
        content = get_book("/home/beregom/Projects/MegaPediki/base/TextAnalyzer/site/library/war_and_piece.txt")
    return content

@app.route("/view")
def viewer():
    #print(name, begin)
    return render_template("/view.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('/404.html'), 404

a = 5
app.run(debug=True, port=5000)