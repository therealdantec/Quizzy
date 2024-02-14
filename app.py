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
        username = request.form['username']
        password = request.form['password']
        users = json.load(open('users.json'))
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('quiz_homepage'))
    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = json.load(open('users.json'))
        users[username] = password
        json.dump(users, open('users.json', 'w'))
        session['username'] = username
        return redirect(url_for('quiz_homepage'))
    return render_template('create_account.html')

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        quiz_name = request.form.get('quiz_name')
        questions = request.form.getlist('questions[]')
        quizzes = []
        for i, question in enumerate(questions):
            answers = request.form.getlist('answers_' + str(i) + '[]')
            correct = request.form.getlist('correct_' + str(i) + '[]')
            quiz = {'quiz name': quiz_name, 'question': question, 'answers': answers, 'correct_answer': correct}
            quizzes.append(quiz)
        with open('quizzes.json', 'r+') as f:
            try:
                existing_quizzes = json.load(f)
            except json.JSONDecodeError:
                existing_quizzes = []
            existing_quizzes.extend(quizzes)
            f.seek(0)
            json.dump(existing_quizzes, f, indent=4)  # Use 4 spaces for indentation
        return redirect(url_for('quiz_homepage'))
    return render_template('create_quiz.html')

@app.route('/quiz_homepage')
def quiz_homepage():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']  # Assuming you're using Flask's session to store the logged-in user
    try:
        with open('quizzes.json', 'r') as f:
            all_quizzes = json.load(f)
    except json.JSONDecodeError:
        all_quizzes = []
    user_quizzes = [quiz for quiz in all_quizzes if quiz.get('username') == username]
    return render_template('quiz_homepage.html', quizzes=user_quizzes)

if __name__ == '__main__':
    app.run(debug=True, port=5500)