from flask import Flask, render_template, request, redirect, url_for

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# index にアクセスしたときの処理


@app.route('/')
def index():
    title = "ペンペペ"

    return render_template("index.html", title=title)


if __name__ == '__main__':
    app.debug = True  # デバッグモード有効化
    app.run()
