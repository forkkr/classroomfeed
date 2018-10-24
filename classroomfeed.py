from flask import Flask, render_template, request, redirect, session
from database.database import db
app = Flask(__name__)


@app.route('/')
def hello_world():
    #data = {'string1': 'string32', 'string2': 'string22'}
    #posts = db.hello_world123
    #post_id = posts.insert_one(data).inserted_id
    return render_template(
        'feed.html', **locals()
    )


if __name__ == '__main__':
    app.run()
