import sys
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings() #创建一个Settings的实例，导入Settings类
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建一艘飞船的实例，导入Ship类
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个用于存储外星人的编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	# Set the background color
	bg_color = (230,230,230)

	# Start the main loop for the game
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(aliens,bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
