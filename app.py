from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json

app = Flask(__name__)


def load_blog_posts():
    """Load blog posts from JSON file.

    Returns:
        list: A list of blog post dictionaries
    """
    with open('blog_posts.json', 'r') as file:
        blog_posts = json.load(file)
    return blog_posts


def save_blog_posts(posts):
    """Save blog posts to JSON file.

    Args:
        posts (list): List of blog post dictionaries to save
    """
    with open('blog_posts.json', 'w') as file:
        json.dump(posts, file, indent=4)


def fetch_post_by_id(post_id):
    """Find and return a post by its ID.

    Args:
        post_id (int): The ID of the post to find

    Returns:
        dict or None: The post dictionary if found, None otherwise
    """
    blog_posts = load_blog_posts()
    for post in blog_posts:
        if post['id'] == post_id:
            return post
    return None


@app.template_filter('dateformat')
def dateformat(date_string):
    """Convert date string to readable format.

    Args:
        date_string (str): Date string in format '%Y-%m-%d %H:%M:%S'

    Returns:
        str: Formatted date string
    """
    if date_string:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        return date_obj.strftime('%B %d, %Y at %I:%M %p')
    return ''


@app.route('/')
def index():
    """Display all blog posts on the home page.

    Returns:
        str: Rendered HTML template with all blog posts
    """
    # Load blog posts from JSON file
    blog_posts = load_blog_posts()

    # Render template with blog posts
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Display add post form on GET, create new post on POST.

    Returns:
        str: Rendered add.html template on GET, redirect to index on POST
    """
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
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'likes': 0
        }

        # Add new post to list
        blog_posts.append(new_post)

        # Save updated posts to JSON file
        save_blog_posts(blog_posts)

        # Redirect to home page
        return redirect(url_for('index'))

    # If GET request, show the form
    return render_template('add.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Display update form on GET, update post on POST.

    Args:
        post_id (int): The ID of the post to update

    Returns:
        str: Rendered update.html on GET, redirect to index on POST,
             or 404 error if post not found
    """
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


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """Delete a blog post by its ID.

    Args:
        post_id (int): The ID of the post to delete

    Returns:
        redirect: Redirect to index page after deletion
    """
    # Load existing posts
    blog_posts = load_blog_posts()

    # Filter out the post with the given id
    blog_posts = [post for post in blog_posts if post['id'] != post_id]

    # Save updated posts to JSON file
    save_blog_posts(blog_posts)

    # Redirect back to home page
    return redirect(url_for('index'))


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    """Increment the like count for a blog post.

    Args:
        post_id (int): The ID of the post to like

    Returns:
        redirect: Redirect to index page after liking
    """
    # Load posts
    blog_posts = load_blog_posts()

    # Find the post and increment likes
    for post in blog_posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            break

    # Save updated posts
    save_blog_posts(blog_posts)

    # Redirect back to home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)