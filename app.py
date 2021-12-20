from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return "тута сайт буит"


@app.route("/movie/")
def srch_title():
    pass


if __name__ == '__main__':
    app.run(debug=True)
