from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is my first post.'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is my second post.'},
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post is None:
        return "Post not found", 404
    return render_template('post_detail.html', post=post)

@app.route('/random/random2')
def randomv():
    return render_template('random.html')

if __name__ == '__main__':
    app.run(debug=True)
