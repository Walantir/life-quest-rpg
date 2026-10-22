from flask import Flask, render_template, request, redirect
from database import init_db, save_cheсkin, get_checkins

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cheсkin", methods=["GET","POST"])
def cheсkin():
    if request.method == "POST":
        weight = request.form["weight"]
        sleep = request.form["sleep"]
        try:
            float(weight)
            float(sleep)
        except:
            return render_template("checkin.html", error="Ошибка, введите число")
        save_cheсkin(weight,sleep)
        return redirect("/stats")
    return render_template("cheсkin.html")

@app.route("/stats")
def stats():
    rows = get_checkins()
    return render_template("stats.html", chekins=rows)

if __name__ == "__main__":
    app.run(debug=True)