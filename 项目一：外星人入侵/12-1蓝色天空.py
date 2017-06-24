import sys

import pygame

def run_game():
	"""初始化游戏并创建一个窗口"""
	pygame.init()
	screen = pygame.display.set_mode((400,400))
	pygame.display.set_caption("蓝色天空")

	#开始游戏的主循环
	while True:
		#监视键盘和鼠标的事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


		#设置游戏的背景色
		bg_color = (0,124,195)
		screen.fill(bg_color)
		ship.blitme()
		#让最近绘制的屏幕可见
		pygame.display.flip()

run_game()