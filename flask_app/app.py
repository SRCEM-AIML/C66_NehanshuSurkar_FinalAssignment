from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        if not name or not age.isdigit():
            return "Invalid input. Please enter a valid name and numeric age."

        return f"Hello {name}, you are {age} years old!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
