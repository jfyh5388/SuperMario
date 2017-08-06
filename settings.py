#coding=utf-8
class Settings():
	#存储《超级马里奥》的所有设置的类
	def __init__(self):
	#初始化游戏的设置
	# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		#self.bg_color = (0, 0, 255)
		self.mario_speed_factor = 1
	
		self.fleet_drop_speed = 1
		self.jump_speed = 2
		self.fall_speed = 3
		self.jump_height = 100

