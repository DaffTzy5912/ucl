from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    lyrics = [
        "Ini adalah lirik pertama",
        "Kemudian lirik kedua berjalan",
        "Lalu lirik ketiga menyusul",
        "Dan seterusnya hingga selesai"
    ]
    return render_template("index.html", lyrics=lyrics)

if __name__ == "__main__":
    app.run(debug=True)
