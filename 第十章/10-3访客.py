filename = 'guest.txt'

while True:
	name = input("Please input your name？")
	if name != '':
		with open(filename, 'a') as file_object:
			file_object.write(name+'\n')
	else:
		break