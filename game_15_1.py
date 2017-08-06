#coding=utf-8
import pygame
from pygame.sprite import Group
from settings import Settings
from mushroom import Mushroom
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

	# ����һ��Ģ��
	mushroom = Mushroom(screen, ai_settings)	
	
	# ��ʼ��Ϸ����ѭ��
	while True:
		# ���Ӽ��̺�����¼�
		
		gf.check_events(mario)		
		mario.update()		
		gf.check_mario_mushroom_collisions(mario, mushroom)
		mushroom.update()
		gf.update_screen(ai_settings, screen, mario, mushroom)	
		
	
			
run_game()
