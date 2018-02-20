from os import remove
from PIL import Image
from MyQR import myqr
from flask import session
import zbarlight,base64,datetime,random

def cus(codes,pic_dir):
	my_qr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+str(random.randint(0,100))+'.png'
	session['dir']=my_qr
	version, level, qr_name = myqr.run(
	codes,
	version=1,
	level='H',
	picture=pic_dir,
	colorized=True,
	contrast=1.0,
	brightness=1.0,
	save_name=my_qr,
	save_dir='/tmp/QR/'
	)
	img_stream = ''
	MyQR = open('/tmp/QR/'+my_qr,'rb')
	img_stream = MyQR.read()
	MyQR.close()
	img_stream = str(base64.b64encode(img_stream))
	img_stream = img_stream[2:(len(img_stream)-3)]
	remove(pic_dir)
	return img_stream