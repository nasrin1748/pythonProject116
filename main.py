from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html file

# About Page
@app.route('/about')
def about():
    return render_template('about.html')  # Renders about.html

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Renders contact.html

if __name__ == '__main__':
    app.run(debug=True)
