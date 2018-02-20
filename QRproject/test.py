from tempfile import NamedTemporaryFile
from PIL import Image
from MyQR import myqr
import zbarlight,ipdb,os, sys

#file_path='./QR.jpg'
with open(file_path,'rb') as image_file:
	image = Image.open(image_file)
	image.load()

codes = str(zbarlight.scan_codes('qrcode',image))
codes = codes[3:(len(codes)-2)]
print('QR codes: %s' % codes)
#ipdb.set_trace()
version, level, qr_name = myqr.run(
	codes,
	version=1,
	level='H',
	picture='out.jpg',
	colorized=True,
	contrast=1.0,
	brightness=1.0,
	save_name='ArtiQR.png',
	save_dir=os.getcwd()
	)