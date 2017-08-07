#coding=utf-8
import pygame
from pygame.sprite import Group
from settings import Settings
from mushroom import Mushroom
from game_status import GameStatus
from mario import Mario
import game_functions as gf
def run_game():
	# ��ʼ����Ϸ������һ����Ļ����
	pygame.init();	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Super Mario")
	
	# ���������
	mario = Mario(screen, ai_settings)

	# ����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��
	status = GameStatus(ai_settings)
	
	# ����һ��Ģ��
	mushroom = Mushroom(screen, ai_settings, status)	
	
	# ��ʼ��Ϸ����ѭ��
	while True:
		# ���Ӽ��̺�����¼�
		
		gf.check_events(mario)		
		if status.game_active:
			mario.update()		
			gf.check_mario_mushroom_collisions(mario, mushroom)
			mushroom.update(status)
		gf.update_screen(ai_settings, screen, mario, mushroom)	
		
	
			
run_game()
