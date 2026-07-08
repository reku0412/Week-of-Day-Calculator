from flask import Flask, render_template, request

app = Flask(__name__)

# ツェラーの公式による曜日計算
def zeller_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    k = year // 100
    j = year % 100

    h = day + (26 * (month + 1) // 10) + 5 * k + (k // 4) + j + (j // 4)
    z = h % 7

    return z


# 曜日の表示
def show_day_of_week(z):
    days = ["土曜日", "日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]
    return days[z]


@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":
        year = int(request.form["year"])
        month = int(request.form["month"])
        day = int(request.form["day"])

        z = zeller_congruence(day, month, year)
        result = show_day_of_week(z)

        result = f"{year}年{month}月{day}日は {result} です"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, port=5001)