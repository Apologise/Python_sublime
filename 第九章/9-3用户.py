class User():
	"""用户类"""

	def __init__(self, first_name, last_name, info, login_attempts):
		"""为last_name和first_name初始化"""
		self.first_name = first_name
		self.last_name = last_name
		self.info = info
		self.login_attempts = login_attempts

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def describe_user(self):
		"""打印用户信息"""
		print(self.first_name + self.last_name + self.info)

	def greet_user(self):
		"""问候用户"""
		print(self.first_name + self.last_name + "你好～")

guy = User("杨","浩","世上最帅的人",0)
guy.describe_user()
guy.greet_user()

print("==============")
print(guy.login_attempts)
guy.increment_login_attempts()
print(guy.login_attempts)
guy.increment_login_attempts()
print(guy.login_attempts)
guy.reset_login_attempts()
print(guy.login_attempts)

