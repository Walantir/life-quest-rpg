from flask import Flask, render_template, request, redirect
from database import init_db, save_checkin, get_checkins
from game import calculate_stats, calculate_streak

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/checkin", methods=["GET","POST"])
def checkin():
    if request.method == "POST":
        weight = request.form["weight"]
        sleep = request.form["sleep"]
        try:
            float(weight)
            float(sleep)
        except:
            return render_template("checkin.html", error="Ошибка, введите число")
        save_checkin(weight,sleep)
        return redirect("/stats")
    return render_template("checkin.html")

@app.route("/stats")
def stats():
    rows = get_checkins()
    streak = calculate_streak(rows)
    if not rows:
        return render_template("stats.html", checkins=rows, stats=None, streak=streak)
    last = rows[-1]
    game_stats = calculate_stats(last[1], last[2], streak)
    return render_template("stats.html", checkin=rows, stats=game_stats, streak=streak)

if __name__ == "__main__":
    app.run(debug=True)