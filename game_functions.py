#coding=utf-8
import sys
import pygame
from mushroom import Mushroom

def check_keydown_events(event, mario):
	#"""响应按键"""
	if event.key == pygame.K_RIGHT:
		mario.moving_right = True
	elif event.key == pygame.K_LEFT:
		mario.moving_left = True
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,mario):
	#"""响应松开"""
	if event.key == pygame.K_RIGHT:
		mario.moving_right = False
	elif event.key == pygame.K_LEFT:
		mario.moving_left = False

def check_events(mario):
	#"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, mario)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, mario)
			
		
def check_mario_mushroom_collisions(mario, mushroom):
	#"""响应马里奥和蘑菇的碰撞"""
	if(mushroom.rect.bottom >= mario.rect.top and mushroom.rect.left <= mario.rect.right and mushroom.rect.right >= mario.rect.left):
		mushroom.eaten = 1

				
def update_screen(ai_settings, screen, mario, mushroom):
	#更新屏幕上的图像，并切换到新屏幕
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)	
	mario.blitme()
	mushroom.blitme()
	# 让最近绘制的屏幕可见
	pygame.display.flip()
	
#def dectet_fire(bullets, aliens):
	#for bullet in bullets.sprites():
		#for alien in aliens.sprites():
			#if(bullet.rect.top <= alien.rect.bottom and bullet.rect.bottom > alien.rect.top and bullet.rect.right >= alien.rect.left and bullet.rect.left <= alien.rect.right):
				#aliens.remove(alien)
