from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def load_blog_posts():
    """Load blog posts from JSON file"""
    with open('blog_posts.json', 'r') as file:
        blog_posts = json.load(file)
    return blog_posts


def save_blog_posts(posts):
    """Save blog posts to JSON file"""
    with open('blog_posts.json', 'w') as file:
        json.dump(posts, file, indent=4)


@app.route('/')
def index():
    # Load blog posts from JSON file
    blog_posts = load_blog_posts()

    # Render template with blog posts
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Load existing posts
        blog_posts = load_blog_posts()

        # Generate new ID (highest ID + 1)
        if blog_posts:
            new_id = max(post['id'] for post in blog_posts) + 1
        else:
            new_id = 1

        # Create new post from form data
        new_post = {
            'id': new_id,
            'author': request.form.get('author'),
            'title': request.form.get('title'),
            'content': request.form.get('content')
        }

        # Add new post to list
        blog_posts.append(new_post)

        # Save updated posts to JSON file
        save_blog_posts(blog_posts)

        # Redirect to home page
        return redirect(url_for('index'))

    # If GET request, show the form
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    # Load existing posts
    blog_posts = load_blog_posts()

    # Filter out the post with the given id
    blog_posts = [post for post in blog_posts if post['id'] != post_id]

    # Save updated posts to JSON file
    save_blog_posts(blog_posts)

    # Redirect back to home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
