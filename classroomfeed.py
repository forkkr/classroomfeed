from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template(
        'feed.html', **locals()
    )


if __name__ == '__main__':
    app.run()
