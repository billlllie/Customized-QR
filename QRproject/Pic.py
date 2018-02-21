from os import remove
from cusqr import cus
from PIL import Image
from flask import redirect,session
import zbarlight,time

def p2t(codes,codes_qr,picname):
	if codes and codes_qr:
			return redirect('/error1')
	elif codes:
		pic_dir = '/tmp/'+picname
		return cus(codes,pic_dir)
	else:
		pic_dir= '/tmp/'+picname
		codes = codes_qr
		codes = codes[3:(len(codes)-2)]
		return cus(codes,pic_dir)
