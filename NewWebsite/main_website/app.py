from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/kerala")
def kerala():
    return render_template("kerala.html")

if __name__ == "__main__":
    app.run(debug=True)
