import json
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'secret'

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
            session['username'] = username  # Add this line
            return redirect(url_for('quiz_homepage'))  # changed from 'create_quiz' to 'home'
    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}  # If the file doesn't exist yet, start with an empty dictionary
        users[username] = password
        with open('users.json', 'w') as f:
            json.dump(users, f)
        session['username'] = username  # Add this line
        return redirect(url_for('quiz_homepage'))  # changed from 'create_quiz' to 'home'
    return render_template('create_account.html')

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        # Get the quiz data from the form
        quiz_name = request.form['quiz_name']
        question = request.form['question']
        answers = request.form.getlist('answers')
        correct_answer = request.form['correct_answer']
        username = session['username']

        # Save the quiz under the username
        quiz = {'quiz name': quiz_name, 'question': question, 'answers': answers, 'correct_answer': correct_answer}
        try:
            with open('quizzes.json', 'r') as f:
                try:
                    quizzes = json.load(f)
                except json.JSONDecodeError:
                    quizzes = {}  # If the file is empty, start with an empty dictionary
        except FileNotFoundError:
            quizzes = {}  # If the file doesn't exist yet, start with an empty dictionary
        if username in quizzes:
            quizzes[username].append(quiz)
        else:
            quizzes[username] = [quiz]
        with open('quizzes.json', 'w') as f:
            json.dump(quizzes, f)

        return redirect(url_for('quiz_homepage'))
    return render_template('create_quiz.html')

@app.route('/quiz')
def quiz_homepage():
    return render_template('quiz_homepage.html')  # assuming you have a home.html in your templates folder

if __name__ == '__main__':
    app.run(debug=True, port=5500)