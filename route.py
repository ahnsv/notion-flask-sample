from flask import Flask

app = Flask(__name__)
@app.route('/')
def notion_page():
    return 'do nothing'

@app.route('/user/<username>')
def notion_user(username):
    return 'User %s' % username

@app.route('/user/<username>/posts')
def notion_user_posts():
    return 'Get posts of the user'

@app.route('/user/<username>/post/<path:post_hash>')
def notion_user_post(post_hash):
    return 'Get user post %s' % post_hash

if __name__ == '__main__':
    app.run()