import pygame

from bullet import Bullet

class Ship():
	"""飞船类"""
	def __init__(self, screen, ai_settings):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings 



		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect   = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 将每艘飞船放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#在飞船的属性center中储存小数值
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_down = False
		self.moving_up = False

		#开火标志
		self.fire_status = False

	def update(self, ai_settings, screen, ship, bullets):
		"""根据飞船位置来调整移动状态"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0: 
			self.centery -= self.ai_settings.ship_speed_factor
#			print("我被按了上")
		if self.moving_down and self.rect.bottom < self.ai_settings.screen_height:
			self.centery += self.ai_settings.ship_speed_factor
#			print("我被按了下")


		#根据self.center更新rect对象
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery


	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)