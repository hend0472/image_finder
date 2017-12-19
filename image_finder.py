import os
import shutil

crap_words = ['background', 'welcome', 'test', 'recycle.bin']
copy_location = os.getcwd() + '\\Pictures_Capture'
current_directory = os.getcwd()[:1]
drive_locations = []
drive_letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
drive_letters.remove(current_directory)

for letter in drive_letters:
	drive_locations.append(letter + ':\\')


def make_directory():
	if os.path.exists(copy_location):
		print('COPY LOCATION EXISTS. CONTINUING.')
	else:
		os.makedirs(copy_location)


def check_directory(directory_to_check):
	for (dirname, dirs, files) in os.walk(directory_to_check):
		for filename in files:
			try:
				if filename.endswith('.jpeg') or filename.endswith('.gif') or filename.endswith('jpg'):
					file = os.path.join(dirname, filename)
					file_size = os.path.getsize(file)
					if int(file_size) > 75000:
						if not any(word.lower() in file for word in crap_words):
							print(file)
							try:
								shutil.copyfile(file, (copy_location + '\\' + filename))
							except Exception as e:
								print(e)
								pass
			except:
				pass


if __name__ == '__main__':
	make_directory()
	# check_directory('C:\\')
	for drive in drive_locations:
		check_directory(drive)
