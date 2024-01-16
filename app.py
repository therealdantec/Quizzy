from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        # Handle the POST request here. For example, you might get the code from the form
        # and use it to join the user to a game.
        code = request.form.get('code')
        # TODO: Add code to handle the game joining logic
    return render_template('join.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # TODO: Add code to check the username and password, and log the user in
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)