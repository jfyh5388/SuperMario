import pygame
from pygame.sprite import Sprite
from random import randint
class Mushroom(Sprite):
	#"""表示单个蘑菇的类"""
	def __init__(self, screen, ai_settings):
	#"""初始化蘑菇并设置其起始位置"""
		super(Mushroom, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# 加载蘑菇图像，并设置其rect属性
		self.image = pygame.image.load('images/mushroom.png')
		self.rect = self.image.get_rect()
		# 每个蘑菇最初都在屏幕左上角附近
		self.rect.x = randint(0, self.screen.get_rect().width-self.rect.width)
		self.rect.y = 0
		# 存储蘑菇的准确位置
		self.x = float(self.rect.x)
		
		self.eaten = 0
		
	def check_edges(self):
		#"""如果蘑菇位于屏幕边缘，就返回True"""
		if self.rect.bottom >= self.screen.get_rect().bottom:
			return True


	def blitme(self):
		#"""在指定位置绘制蘑菇""
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		if(self.check_edges() or self.eaten == 1):
			self.rect.x = randint(0, self.screen.get_rect().width-self.rect.width)
			self.rect.y = 0
			self.eaten = 0
		else:			
			self.rect.y += self.ai_settings.fleet_drop_speed
