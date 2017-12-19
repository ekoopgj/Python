import sys
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings() #创建一个Settings的实例，导入Settings类
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建play按钮
	play_button = Button(ai_settings, screen, "play")
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
	#创建一个用于存储游戏统计信息的实例,并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# Start the main loop for the game
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
			#gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
