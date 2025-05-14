from flask import Flask, render_template, request
import os

# Set the correct path to the templates folder
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend/templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('fname')
    email = request.form.get('email')
    message = request.form.get('message')

    return f"Hello {name}, your message has been received!"

if __name__ == '__main__':
    app.run(debug=True)
