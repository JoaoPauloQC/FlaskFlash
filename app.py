from flask import Flask, render_template, url_for, request, make_response, redirect


app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')





if __name__ == '__main__':
    app.run(debug=True)
