#coding=utf-8
import pygame
from pygame.sprite import Group
from settings import Settings
from mushroom import Mushroom
from game_status import GameStatus
from mario import Mario
import game_functions as gf
def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init();	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Super Mario")
	
	# 创建马里奥
	mario = Mario(screen, ai_settings)

	# 创建一个用于存储游戏统计信息的实例
	status = GameStatus(ai_settings)
	
	# 创建一个蘑菇
	mushroom = Mushroom(screen, ai_settings, status)	
	
	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		
		gf.check_events(mario)		
		if status.game_active:
			mario.update()		
			gf.check_mario_mushroom_collisions(mario, mushroom)
			mushroom.update(status)
		gf.update_screen(ai_settings, screen, mario, mushroom)	
		
	
			
run_game()
