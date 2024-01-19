import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/join_quiz', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        # Handle the POST request here. For example, you might get the code from the form
        # and use it to join the user to a game.
        code = request.form.get('code')
        # TODO: Add code to handle the game joining logic
    return render_template('join_quiz.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('users.json', 'r') as f:
            users = json.load(f)
        if username in users and users[username] == password:
            return redirect(url_for('create_quiz'))
    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('users.json', 'r') as f:
            users = json.load(f)
        users[username] = password
        with open('users.json', 'w') as f:
            json.dump(users, f)
        return redirect(url_for('create_quiz'))
    return render_template('create_account.html')

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    # TODO: Add code to handle quiz creation
    return render_template('create_quiz.html')

if __name__ == '__main__':
    app.run(debug=True)