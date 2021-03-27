import os

def recursor(dirpath):
	print(dirpath)
	with os.scandir(dirpath) as it:
		for entry in it:
			if entry.name.endswith(".HEIC") and entry.is_file():
				# print(entry.name, entry.path)
				npath = entry.path.split('.')
				npath.pop()
				npath.append('jpg')
				npath = '.'.join(npath)
				os.rename(entry.path, npath)
			else:
				if not entry.is_file():
					# directory
					recursor(entry.path)


recursor(os.path.dirname(os.path.realpath(__file__)))
