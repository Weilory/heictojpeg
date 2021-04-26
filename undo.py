import os


def recursor(dirpath):
	# print(dirpath)
	with os.scandir(dirpath) as it:
		for entry in it:
			if entry.name.endswith(".JPEG") and entry.is_file():
				# print(entry.name, entry.path)
				os.remove(entry.path)
				print('removed ', entry.path)
			else:
				if not entry.is_file():
					# directory
					recursor(entry.path)


recursor(os.path.dirname(os.path.realpath(__file__)))
