import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#设置游戏的背景色 
	bg_color = (230, 230, 230)

	#创建一艘飞船
	ship = Ship(screen, ai_settings)

	#创建一个外星人实例
	alien = Alien(ai_settings, screen)

	#创建一个用于储存子弹的编组
	bullets = Group()
	#创建外星人群
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship,aliens)

	#创建一个用于储存统计信息的实例
	stats = GameStats(ai_settings)

	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")

	#开始游戏的主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats,play_button,ship, aliens,bullets)
		if stats.game_active:
			ship.update(ai_settings, screen, ship, bullets)
			gf.update_bullets(ai_settings, screen, ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats, screen,ship,aliens, bullets)

		gf.update_screen(ai_settings, screen, stats,ship, aliens,bullets, play_button)



run_game()