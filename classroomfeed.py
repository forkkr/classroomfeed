from bson import ObjectId
from flask import Flask, render_template, request, redirect, session
from database.database import db
app = Flask(__name__)


@app.route('/')
def hello_world():
    #data = {'string1': 'string32', 'string2': 'string22'}
    #posts = db.hello_world123
    #post_id = posts.insert_one(data).inserted_id
    return redirect('/news-feed')


@app.route("/news-feed")
def show_news_feed():
    pymongo_cursor = db.hello_world123.find()
    all_data = list(pymongo_cursor)
    data = all_data
    print(data)
    return render_template('feed.html', **locals())


@app.route("/entry_data" , methods=['POST', 'GET'])
def update_post():
    if request.method=="POST":
        data = request.form
        data = {"posttext": data['message'],"postfile": data['files'] , "authors": "forkkr"}
        posts = db.hello_world123
        post_id = posts.insert_one(data).inserted_id
    return redirect('/news-feed')


@app.route("/comment_entry/<id>" , methods=['POST', 'GET'])
def comment_entry(id):
    poststring=db.hello_world123.find_one({'_id': ObjectId(id)});
    pymongo_cursor = db.comments.find( { "postid" : id} )
    all_comments = list(pymongo_cursor)
    comments= all_comments
    print(comments)
    return render_template('comment.html' ,poststring=poststring, comments=comments)


@app.route("/entry_comment/<id>" , methods=['POST', 'GET'])
def update_comment(id):
    if request.method=="POST":
        data = request.form
        data = {"posttext": data['message'],"postid":id ,  "authors": "forkkr"}
        posts = db.comments
        post_id = posts.insert_one(data).inserted_id
    return redirect('/comment_entry/'+str(id))


if __name__ == '__main__':
    app.run()
