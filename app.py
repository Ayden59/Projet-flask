from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/localisation")
def localisation():
    return render_template("localisation.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)