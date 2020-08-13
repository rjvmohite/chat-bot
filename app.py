from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        return render_template("index.html", title = "ChatBot", chat_response = request.form["msg"])
    else:
        return render_template("index.html",title = "ChatBot")


@app.route("/about")
def about():
    return render_template("about.html",title = "About Me", content="...never stop exploring...")


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)