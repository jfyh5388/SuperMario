import pygame
from pygame.sprite import Sprite
from random import randint
class Mushroom(Sprite):
	#"""��ʾ����Ģ������"""
	def __init__(self, screen, ai_settings):
	#"""��ʼ��Ģ������������ʼλ��"""
		super(Mushroom, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# ����Ģ��ͼ�񣬲�������rect����
		self.image = pygame.image.load('images/mushroom.png')
		self.rect = self.image.get_rect()
		# ÿ��Ģ�����������Ļ���ϽǸ���
		self.rect.x = randint(0, self.screen.get_rect().width-self.rect.width)
		self.rect.y = 0
		# �洢Ģ����׼ȷλ��
		self.x = float(self.rect.x)
		
		self.eaten = 0
		
	def check_edges(self):
		#"""���Ģ��λ����Ļ��Ե���ͷ���True"""
		if self.rect.bottom >= self.screen.get_rect().bottom:
			return True


	def blitme(self):
		#"""��ָ��λ�û���Ģ��""
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		if(self.check_edges() or self.eaten == 1):
			self.rect.x = randint(0, self.screen.get_rect().width-self.rect.width)
			self.rect.y = 0
			self.eaten = 0
		else:			
			self.rect.y += self.ai_settings.fleet_drop_speed
