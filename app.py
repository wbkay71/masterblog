from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)


@app.template_filter('dateformat')
def dateformat(date_string):
    """Convert date string to readable format"""
    if date_string:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        return date_obj.strftime('%B %d, %Y at %I:%M %p')
    return ''


def load_blog_posts():
    """Load blog posts from JSON file"""
    with open('blog_posts.json', 'r') as file:
        blog_posts = json.load(file)
    return blog_posts


def save_blog_posts(posts):
    """Save blog posts to JSON file"""
    with open('blog_posts.json', 'w') as file:
        json.dump(posts, file, indent=4)

def fetch_post_by_id(post_id):
    """Find and return a post by its ID"""
    blog_posts = load_blog_posts()
    for post in blog_posts:
        if post['id'] == post_id:
            return post
    return None

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
            'content': request.form.get('content'),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Load all posts
        blog_posts = load_blog_posts()

        # Find and update the post
        for p in blog_posts:
            if p['id'] == post_id:
                p['author'] = request.form.get('author')
                p['title'] = request.form.get('title')
                p['content'] = request.form.get('content')
                break

        # Save updated posts
        save_blog_posts(blog_posts)

        # Redirect back to index
        return redirect(url_for('index'))

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
