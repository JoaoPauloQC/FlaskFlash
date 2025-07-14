from flask import Flask, render_template, url_for, request, make_response, redirect


app = Flask(__name__)

nomes = ["joao", "ale", "pedro"]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/singin', methods=["POST", "GET"])
def signin():
    name = request.form['nameform']
    if name in nomes:
        return redirect(url_for('home'))
    
@app.route('/home')
def home():
    return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True)
