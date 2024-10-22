from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with an input form
html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome Page</title>
    </head>
    <body>
        <h1>Enter your name</h1>
        <form method="POST" action="/">
            <input type="text" name="username" placeholder="Enter your name" required>
            <button type="submit">Submit</button>
        </form>
        {% if name %}
        <h2>Welcome, {{ name }}!</h2>
        {% endif %}
    </body>
    </html>
'''

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    name = None
    if request.method == 'POST':
        name = request.form.get('username')  # Get the username from the form
    return render_template_string(html_template, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
