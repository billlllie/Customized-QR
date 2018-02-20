from os import remove
import zbarlight
from cusqr import cus
from PIL import Image

def p2t(codes,qrname,picname):
	if codes and qrname:
			return none
	elif codes:
		pic_dir = '/tmp/QR/'+picname
		return cus(codes,pic_dir)
	else:
		qr_dir= '/tmp/QR/'+qrname
		pic_dir= '/tmp/QR/'+picname
		with open(qr_dir,'rb') as img_file:
			QR = Image.open(img_file)
			QR.load()
		codes = str(zbarlight.scan_codes('qrcode',QR))
		codes = codes[3:(len(codes)-2)]
		QR.close()
		remove(qr_dir)
		return cus(codes,pic_dir)
