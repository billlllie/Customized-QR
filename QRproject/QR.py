from flask import Flask,render_template,request,send_file,redirect,url_for,session,abort


UPLOAD_FOLDER = '/tmp/QR/'
result = None
my_qr = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
	from PIL import Image
	from Pic import p2t
	from io import StringIO
	from werkzeug import secure_filename
	import os
	global result
	codes = request.form.get('inputurl')
	qr = request.files.get('QR')
	pic = request.files.get('Pic')
	if qr == None:
		qrb = False
	else:
		qrb = True
	if bool(codes) & qrb:
		return redirect('/error1')
	elif pic == None:
		return redirect('/error2')
	elif bool(codes) == False and qrb == False:
		return redirect('/error3')
	else:
		qrname = secure_filename(qr.filename)
		picname = secure_filename(pic.filename)
		qr.save((os.path.join(app.config['UPLOAD_FOLDER'], qrname)))
		pic.save((os.path.join(app.config['UPLOAD_FOLDER'], picname)))
		result = p2t(codes,qrname,picname)
		return redirect('/result')

@app.route('/result')
def result():
	global result
	img_stream = result
	return render_template('result.html',img_stream=img_stream)

@app.route('/download',methods=['POST'])
def download():
	from tempfile import NamedTemporaryFile
	from shutil import copyfileobj
	from os import remove
	my_qr = session['dir']
	tempFileObj = NamedTemporaryFile(mode='w+b',suffix='png')
	MyQR = open('/tmp/QR/'+my_qr,'rb')
	copyfileobj(MyQR,tempFileObj)
	MyQR.close()
	remove('/tmp/QR/'+my_qr)
	tempFileObj.seek(0,0)
	response = send_file(tempFileObj, as_attachment=True, attachment_filename='MyQR.png')
	return response

@app.route('/error1')
def error1():
	return render_template('error1.html')

@app.route('/error2')
def error2():
	return render_template('error2.html')

@app.route('/error3')
def error3():
	return render_template('error3.html')

if __name__ == '__main__':
	app.debug = True
	app.run()


