from flask import Flask, render_template, request
from aligner import pij_aligner

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        target = request.form.get("target")
        query = request.form.get("query")
        mode = request.form.get("mode")

        result = pij_aligner(target, query, mode)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
