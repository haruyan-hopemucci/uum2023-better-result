# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template
import app.scrp as scrp

# Flaskオブジェクトの生成
app = Flask(__name__)


# 「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    srcTable, runnerCount = scrp.scrapeUnion()
    # return render_template("index.html", srcTable=srcTable, runnerCount=runnerCount)
    # print(runnerCount)
    return render_template("index.html", srcTable=srcTable, runnerCount=runnerCount)


# 「/index」へアクセスがあった場合に、「index.html」を返す
@ app.route("/index")
def index():
    return hello()


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
