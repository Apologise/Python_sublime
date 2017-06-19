def get_formatted_named(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name

musician = get_formatted_named('jimi', 'hendrix')
print(musician)