import os
import pyheif
from PIL import Image


def heic2jpg(path, npath):
    heif_file = pyheif.read(path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )

    image.save(npath, "JPEG")
    print('created ', npath)



def recursor(dirpath):
	# print(dirpath)
	with os.scandir(dirpath) as it:
		for entry in it:
			if entry.name.endswith(".HEIC") and entry.is_file():
				# print(entry.name, entry.path)
				npath = entry.path.split('.')
				npath.pop()
				npath.append('JPEG')
				npath = '.'.join(npath)
				heic2jpg(entry.path, npath)
			else:
				if not entry.is_file():
					# directory
					recursor(entry.path)


recursor(os.path.dirname(os.path.realpath(__file__)))
