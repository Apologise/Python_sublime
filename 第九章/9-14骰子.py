from random import randint

class Die():
	"""模拟一个骰子的过程"""

	def __init__(self, sides = 6):
		"""初始化骰子的面数属性"""
		self.sides = sides

	def roll_die(self):
		"""随机丢骰子"""
		x = randint(1, self.sides)
		print(str(x), end = ' ')
die = Die()
for i in range(10):
	die.roll_die()
print("\n=========")
die1 = Die(10)
for i in range(10):
	die1.roll_die()
print("\n=========")
die2 = Die(20)
for i in range(10):
	die2.roll_die()
