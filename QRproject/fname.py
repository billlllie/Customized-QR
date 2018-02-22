from pypinyin import lazy_pinyin
from werkzeug import secure_filename

def check_name(filename):
	if filename.startswith('.'):
	    name = files.filename.split('.')[0]
	    ext = files.filename.split('.')[1]
	    filename = '_'.join(lazy_pinyin(name)) + '.' + ext
	    return filename
	else:
		return filename