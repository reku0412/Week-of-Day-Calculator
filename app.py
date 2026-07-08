from flask import Flask, render_template, request
from datetime import datetime

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

        try:
            # HTMLから受け取る
            date = request.form["date"]

            # 年月日に分割
            year, month, day = map(int, date.split("-"))

            # 日付が存在するかチェック
            datetime(year, month, day)

            # 曜日計算
            z = zeller_congruence(day, month, year)
            weekday = show_day_of_week(z)

            result = f"{year}年{month}月{day}日は {weekday} です"

        except ValueError:
            result = "⚠️ 無効な日付です。正しい日付を入力してください。"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)