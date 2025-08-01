# Masterblog - Flask Blog Application

A simple and elegant blog application built with Flask, featuring a modern dark theme and full CRUD functionality.

## Features

- 📝 **Create** new blog posts
- 📖 **Read** all blog posts on the home page
- ✏️ **Update** existing posts
- 🗑️ **Delete** posts
- ❤️ **Like** posts (currently unlimited)
- 🕐 **Timestamps** for each post
- 🎨 **Modern dark theme** with smooth animations
- 💾 **JSON-based storage** for simplicity

## Technologies Used

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Storage**: JSON file-based storage
- **Styling**: Custom CSS with CSS Variables

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd masterblog
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask
```

## Project Structure

```
masterblog/
├── app.py              # Main Flask application
├── blog_posts.json     # Data storage file
├── static/
│   └── style.css      # Custom CSS styles
└── templates/
    ├── index.html     # Home page template
    ├── add.html       # Add post form
    └── update.html    # Update post form
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5001
```

Note: The application runs on port 5001 by default. You can change this in `app.py` if needed.

## Usage

### Adding a Post
1. Click the "✨ Add New Post" button on the home page
2. Fill in the author name, title, and content
3. Click "Add Post" to publish

### Updating a Post
1. Click the "Update" button on any post
2. Modify the fields you want to change
3. Click "Update Post" to save changes

### Deleting a Post
1. Click the "Delete" button on any post
2. The post will be immediately removed

### Liking a Post
1. Click the "❤️ Like" button on any post
2. The like counter will increase

## Data Storage

Blog posts are stored in `blog_posts.json` with the following structure:
```json
{
    "id": 1,
    "author": "John Doe",
    "title": "Post Title",
    "content": "Post content...",
    "created_at": "2025-08-01 13:42:00",
    "likes": 0
}
```

## Known Limitations

- **Likes**: Currently, users can like posts multiple times. Future versions could implement session-based or authentication-based restrictions.
- **No user authentication**: All visitors have full CRUD access
- **No pagination**: All posts are displayed on one page
- **Basic text formatting**: No rich text editor or Markdown support

## Future Enhancements

- [ ] User authentication and authorization
- [ ] One like per user limitation
- [ ] Rich text editor for post content
- [ ] Post categories and tags
- [ ] Search functionality
- [ ] Pagination for better performance
- [ ] Comments on posts
- [ ] Database integration (SQLite/PostgreSQL)

## Contributing

This is a learning project created as part of the Masterschool bootcamp. Feel free to fork and experiment!

## License

This project is open source and available for educational purposes.