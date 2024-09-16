from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Here you would typically validate the username and password
    # and redirect to a different page if successful
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)
