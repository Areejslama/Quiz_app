from flask import Flask,  render_template, url_for

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def welcome():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
