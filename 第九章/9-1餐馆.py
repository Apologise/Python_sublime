class Restaurant():
	"""模拟餐馆"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def set_number_served(self, value):
		self.number_served = value

	def increment_number_served(self, increment):
		self.increment_number_served += increment

	def decribe_restaurant(self):
		"""打印类的两个属性"""
		print(self.restaurant_name+self.cuisine_type)

	def open_restaurant(self):
		"""显示餐馆的营业状态"""
		print("餐馆正在营业")

restaurant = Restaurant('每日一餐', '早餐')
restaurant.decribe_restaurant()
restaurant.open_restaurant()
