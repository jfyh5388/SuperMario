#coding=utf-8
import pygame
class Mario():
	def __init__(self, screen, settings):
		#��ʼ������²��������ʼλ��
		self.screen = screen
		self.ai_settings = settings
		# ���������ͼ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('images/mario.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# ��ÿ��������·�����Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# ������µ�����center�д洢С��ֵ
		self.centerx = float(self.rect.centerx)
		# �ƶ���־
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		#"""�����ƶ���־��������µ�λ��"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.mario_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.mario_speed_factor
			
		# ����self.center����rect����
		self.rect.centerx = self.centerx
			
	def blitme(self):
		#��ָ��λ�û��������
		self.screen.blit(self.image, self.rect)

