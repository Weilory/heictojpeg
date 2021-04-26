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


ans = input('Are you sure? this will remove all JPEG files despite of whether it is created by heictojpg.py in current directory and all sub-directories belongs in? (y/n)')
ans = ans.strip()
if ans == 'y' or ans == 'Y':
	recursor(os.path.dirname(os.path.realpath(__file__)))
else:
	print('undo aborted')
