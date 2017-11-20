from flask import render_template, request
from app import app
import process_form as pf


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/form')
def form():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('form.html',
                           title='Home',
                           user=user)
@app.route('/handle_data', methods=['POST'])
def handle_data():

	pf.process_data(request)

    #nama_depan = 'izak'
    #projectpath = request.form['projectFilepath']
    # your code
    # return a response
	user = {'nickname': 'Miguel'}  # fake user
	return render_template('index.html',
                           title='Hasil',
                           user=user)
