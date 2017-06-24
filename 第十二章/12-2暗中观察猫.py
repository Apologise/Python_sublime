import sys

import pygame

from cat import Cat


def run_game():
	"""初始化游戏并创建一个窗口"""
	pygame.init()
	screen = pygame.display.set_mode((400,400))
	pygame.display.set_caption("暗中观察猫")

	# 创建一个暗中观察猫的实例
	#cat1 = Cat(screen)
	ship = Cat(screen)

	#开始游戏的主循环
	while True:
		#监视键盘和鼠标的事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			

		#设置游戏的背景色
		bg_color = (230,230,230)
		screen.fill(bg_color)
		ship.blitme()
		#让最近绘制的屏幕可见
		pygame.display.flip()

run_game()