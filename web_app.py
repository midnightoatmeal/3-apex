
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        arxiv_id = request.form["arxiv_id"]
        return f"Recieved arxiv ID: {arxiv_id}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)