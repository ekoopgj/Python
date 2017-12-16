import sys
import pygame
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
	ship = Ship(screen)

	## Set the background color
	bg_color = (230,230,230)

	# Start the main loop for the game
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)

run_game()
