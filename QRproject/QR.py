from flask import Flask,render_template,request,send_file,redirect,url_for,make_response,Response

UPLOAD_FOLDER = '/tmp/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'   // generate a random key for yourself

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
	from PIL import Image
	from Pic import p2t
	from io import StringIO
	from werkzeug import secure_filename
	from fname import check_name
	from os import remove
	import os,zbarlight,time
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
		picname = check_name(pic.filename)
		pic.save((os.path.join(app.config['UPLOAD_FOLDER'], picname)))
		if qrb:
			qrname = check_name(qr.filename)
			qr.save((os.path.join(app.config['UPLOAD_FOLDER'], qrname)))
			with open('/tmp/'+qrname,'rb') as img_file:
				QR = Image.open(img_file)
				QR.load()
			codes_qr = str(zbarlight.scan_codes('qrcode',QR))
			QR.close()
			remove('/tmp/'+qrname)
			if codes_qr == 'None':
				return redirect('/error4')
			else:
				return p2t(codes,codes_qr,picname)
		else:
			qrname = False
			return p2t(codes,qrname,picname)

@app.route('/result')
def result():
	import base64
	my_dir = '/tmp/'+request.cookies.get('dir')
	img_stream = ''
	MyQR = open(my_dir,'rb')
	img_stream = MyQR.read()
	MyQR.close()
	img_stream = str(base64.b64encode(img_stream))
	img_stream = img_stream[2:(len(img_stream)-3)]
	return render_template('result.html',img_stream=img_stream)

@app.route('/download',methods=['POST'])
def download():
	from tempfile import NamedTemporaryFile
	from shutil import copyfileobj
	from os import remove
	my_qr = request.cookies.get('dir')
	tempFileObj = NamedTemporaryFile(mode='w+b',suffix='png')
	MyQR = open('/tmp/'+my_qr,'rb')
	copyfileobj(MyQR,tempFileObj)
	MyQR.close()
	remove('/tmp/'+my_qr)
	tempFileObj.seek(0,0)
	res = make_response(send_file(tempFileObj, as_attachment=True, attachment_filename='MyQR.png'))
	res.set_cookie('dir', '', expires=0)
	return send_file(tempFileObj, as_attachment=True, attachment_filename='MyQR.png')

@app.route('/error1')
def error1():
	return render_template('error1.html')

@app.route('/error2')
def error2():
	return render_template('error2.html')

@app.route('/error3')
def error3():
	return render_template('error3.html')

@app.route('/error4')
def error4():
	return render_template('error4.html')

if __name__ == '__main__':
	app.run()


