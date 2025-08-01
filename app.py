from flask import Flask, render_template
import json

app = Flask(__name__)


def load_blog_posts():
    """Load blog posts from JSON file"""
    with open('blog_posts.json', 'r') as file:
        blog_posts = json.load(file)
    return blog_posts


@app.route('/')
def index():
    # Load blog posts from JSON file
    blog_posts = load_blog_posts()

    # Render template with blog posts
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
