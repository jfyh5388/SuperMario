#coding=utf-8
import sys
import pygame
from mushroom import Mushroom

def check_keydown_events(event, mario):
	#"""��Ӧ����"""
	if event.key == pygame.K_RIGHT:
		mario.moving_right = True
	elif event.key == pygame.K_LEFT:
		mario.moving_left = True
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,mario):
	#"""��Ӧ�ɿ�"""
	if event.key == pygame.K_RIGHT:
		mario.moving_right = False
	elif event.key == pygame.K_LEFT:
		mario.moving_left = False

def check_events(mario):
	#"""��Ӧ����������¼�"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, mario)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, mario)
			
		
def check_mario_mushroom_collisions(mario, mushroom):
	#"""��Ӧ����º�Ģ������ײ"""
	if(mushroom.rect.bottom >= mario.rect.top and mushroom.rect.left <= mario.rect.right and mushroom.rect.right >= mario.rect.left):
		mushroom.eaten = 1

				
def update_screen(ai_settings, screen, mario, mushroom):
	#������Ļ�ϵ�ͼ�񣬲��л�������Ļ
	# ÿ��ѭ��ʱ���ػ���Ļ
	screen.fill(ai_settings.bg_color)	
	mario.blitme()
	mushroom.blitme()
	# ��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
	
#def dectet_fire(bullets, aliens):
	#for bullet in bullets.sprites():
		#for alien in aliens.sprites():
			#if(bullet.rect.top <= alien.rect.bottom and bullet.rect.bottom > alien.rect.top and bullet.rect.right >= alien.rect.left and bullet.rect.left <= alien.rect.right):
				#aliens.remove(alien)
