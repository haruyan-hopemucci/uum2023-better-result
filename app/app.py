# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template
import app.scrp as scrp

# Flaskオブジェクトの生成
app = Flask(__name__)


# 「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    srcTable, runnerCount = scrp.scrapeUnionDay2()
    return render_template("index.html", srcTable=srcTable, runnerCount=runnerCount, day=2)


# 「/index」へアクセスがあった場合に、「index.html」を返す
@ app.route("/index")
def index():
    return hello()


@app.route("/day1")
def day1():
    srcTable, runnerCount = scrp.scrapeUnionDay1()
    return render_template("day.html", srcTable=srcTable, runnerCount=runnerCount, day=1)


@app.route("/day2")
def day2():
    srcTable, runnerCount = scrp.scrapeUnionDay2()
    return render_template("day.html", srcTable=srcTable, runnerCount=runnerCount, day=2)


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
