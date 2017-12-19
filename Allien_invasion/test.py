import sys
import pygame
import pygame.font  #让Pygame将文本渲染到屏幕上

class Button():

	def __init__(self, ai_settings, screen, msg):
		"""初始化按钮的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#设置按钮的尺寸和其他属性
		self.width, self.height = 200,50
		self.button_color = (0,255,0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		#创建按钮的rect对象， 并使其居中
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		# 按钮的标签只创建一次
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""将msg渲染到图像，并使其在按钮上居中"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		#绘制一个用颜色填充的按钮,再绘制文本
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings() #创建一个Settings的实例，导入Settings类
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建play按钮
	play_button = Button(ai_settings, screen, "play")

	# Set the background color
	bg_color = (230,230,230)


	# Start the main loop for the game
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens,bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			#gf.update_screen(ai_settings, screen, ship, aliens, bullets)
			gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
