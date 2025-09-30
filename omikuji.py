from flask import Flask, render_template, request
import random

app = Flask(__name__)

OMIKUJI = ["大吉", "中吉", "小吉"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        result = random.choice(OMIKUJI)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)