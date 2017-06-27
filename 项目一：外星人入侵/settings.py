class Settings():
	"""储存《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 400
		self.screen_height = 450
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 0.1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullet_speed_factor = 1
		self.bullets_allowed = 10
		self.alien_speed_factor = 0.6
		self.fleet_drop_speed = 10
		self.fleet_direction = 1