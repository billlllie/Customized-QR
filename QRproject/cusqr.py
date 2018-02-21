from os import remove
from PIL import Image
from MyQR import myqr
from flask import redirect,make_response,request,session
import zbarlight,datetime,random,time

def cus(codes,pic_dir):
	my_qr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+str(random.randint(0,100))+'.png'
	res = make_response(redirect('/result'))
	res.set_cookie(key='dir',value=my_qr, expires=time.time()+6*60)
	version, level, qr_name = myqr.run(
	codes,
	version=1,
	level='H',
	picture=pic_dir,
	colorized=True,
	contrast=1.0,
	brightness=1.0,
	save_name=my_qr,
	save_dir='/tmp/'
	)
	remove(pic_dir)
	return res