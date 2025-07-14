from flask import Flask, render_template, url_for, request, make_response, redirect,flash


app = Flask(__name__)
app.secret_key = "oloco"

nomes = ["joao", "ale", "pedro"]

name_selected = "Guest"

@app.route('/')
def login():
    if request.cookies.get('username'):
        global name_selected
        name_selected = request.cookies.get('username')
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/singin', methods=["POST", "GET"])
def signin():
    name = request.form['nameform']
    email = request.form['emailform']
    
    if name in nomes:
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('username',name , max_age=1000)
        resp.set_cookie('email',email, max_age=1000)
        global name_selected
        name_selected = name
        flash('Login bem sucedido!')
        return resp
    else:
        return redirect(url_for('login'))
    
@app.route('/getcookies')
def getcookies():
    resp = make_response('cookies')
    cookies = request.cookies
    return cookies

@app.route('/deletecookies')
def deletecookies():
    resp = make_response('deleting cookies')
    resp.delete_cookie('username')
    resp.delete_cookie('email')
    return resp

@app.route('/home')
def home():
    return render_template("home.html", name=name_selected)



if __name__ == '__main__':
    app.run(debug=True)
