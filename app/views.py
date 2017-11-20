from flask import render_template, request, redirect≈
from app import app
import process_form as pf


@app.route('/')
@app.route('/index')
def index():

    return redirect("http://kader.jaskapital.com/form", code=302)
#    user = {'nickname': 'Miguel'}  # fake user
#    return render_template('index.html',
#                           title='Home',
#                           user=user)

@app.route('/form')
def form():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('form.html',
                           title='Home',
                           user=user)
@app.route('/handle_data', methods=['POST'])
def handle_data():

	pf.process_data(request)
	nama = request.form['nama_depan_saya'] + " " + request.form['nama_belakang_saya']
	email = request.form['email']

	user = {'nickname': nama,
          'email': email}  # fake user
	return render_template('setelah_pendaftaran.html',
                           title='Terima kasih!',
                           user=user)
