magicians = ['杨浩','刘谦','我','我']

def make_great(lists):
	for i in range(len(lists)):
		lists[i] = "The Great" + lists[i]

def show_magicians():
	for i in range(len(magicians)):
		print(magicians[i])

make_great(magicians[:])
show_magicians()