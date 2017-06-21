import json

def greet_user():
	"""问候用户，并指出其名字"""
	filename = 'username.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		username = input('What is your name?')
		with open(filename, 'w') as file_object:
			json.dump(username, file_object)
	else:
		print('Welcome back,' + username + '!')

greet_user()