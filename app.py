from flask import Flask, render_template

app = Flask(__name__)

# Sample data for blog posts
posts = [
    {
        'title': 'First post',
        'content': 'This is my first blog post!',
        'date_posted': 'April 20, 2023'
    },
    {
        'title': 'Second post',
        'content': 'This is my second blog post!',
        'date_posted': 'April 21, 2023'
    }
]

# Home page
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

# About page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
