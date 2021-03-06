#coding=utf-8
import pygame
class Mario():
	def __init__(self, screen, settings):
		#初始化马里奥并设置其初始位置
		self.screen = screen
		self.ai_settings = settings
		# 加载马里奥图像并获取其外接矩形
		self.image = pygame.image.load('images/mario.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# 将每艘新马里奥放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# 在马里奥的属性center中存储小数值
		self.centerx = float(self.rect.centerx)
		# 移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		
	def update(self):
		#"""根据移动标志调整马里奥的位置"""		
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.mario_speed_factor
			
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.mario_speed_factor
		
		if self.moving_up and self.rect.y > self.screen_rect.height - self.ai_settings.jump_height - self.rect.height:			
			self.rect.centery -= self.ai_settings.jump_speed
		
		elif self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.ai_settings.fall_speed
			#下落时若马里奥底部超过屏幕底部,则使其等于屏幕底部
			if self.rect.bottom > self.screen_rect.bottom:
				self.rect.bottom = self.screen_rect.bottom
			self.moving_up = False
		
		# 根据self.center更新rect对象
		self.rect.centerx = self.centerx
			
	def blitme(self):
		#在指定位置绘制马里奥
		self.screen.blit(self.image, self.rect)

