from flask import Flask, render_template, request, redirect
app = Flask(__name__)

dev = True

@app.route('/')
def my_portfolio():
    return render_template('index.html')

@app.route('/ninjas')
def about_me():
    return render_template('ninjas.html') 

@app.route('/dojos')
def my_projects():
    return render_template('dojos.html') 

@app.route('/dojos', methods=['POST'])
def create_user():
    print "Got user info"
    name = request.form['name']
    email = request.form['email']
    print name, email
    return redirect('/')

app.run(debug=dev)