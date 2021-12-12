# candy_corn_catcher.py
# Prototype for basic arcade game. Collect falling candy & score points.
# Author: Jackie P, aka TheDataElemental


# Import built-in modules
import sys
import random
import time
import math
import os

import pygame


# Player sprite with image and x & y coordinates
class Player:
	def __init__(self, image_list, x_start, y_start):
		self.image_list = image_list # TODO: list of images / animation
		self.current_image = self.image_list[0]
		self.x = x_start
		self.y = y_start

# Falling candy corns that player tries to catch
class Candy:
	def __init__(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y

# Start game window
pygame.init()
screen = pygame.display.set_mode((512, 480), \
	pygame.HWSURFACE | pygame.DOUBLEBUF, vsync = 1)
pygame.display.set_caption("CANDY CORN CATCHER")
CCC_icon = pygame.image.load("Assets/Exports/CCC.ico")
pygame.display.set_icon(CCC_icon)

# Import assets
starry_night = pygame.image.load\
	("Assets/Exports/starry_night.png").convert()
moon_img = pygame.image.load\
	("Assets/Exports/moon.png").convert()
cloud_img = pygame.image.load\
	("Assets/Exports/cloud.png").convert()
	
pumpkin_img_1 = pygame.image.load\
	("Assets/Exports/pumpkin_1_flying_jack_1.png").convert_alpha()
pumpkin_img_2 = pygame.image.load\
	("Assets/Exports/pumpkin_1_flying_jack_2.png").convert_alpha()
pumpkin_img_3 = pygame.image.load\
	("Assets/Exports/pumpkin_1_flying_jack_3.png").convert_alpha()
pumpkin_img_4 = pygame.image.load\
	("Assets/Exports/pumpkin_1_flying_jack_4.png").convert_alpha()
pumpkin_images = \
	[pumpkin_img_1, pumpkin_img_2, pumpkin_img_3, pumpkin_img_4]
	
candy_corn_img_1 = pygame.image.load\
	("Assets/Exports/candy_corn_1.png").convert_alpha()
candy_corn_img_2 = pygame.image.load\
	("Assets/Exports/candy_corn_2.png").convert_alpha()
candy_corn_img_3 = pygame.image.load\
	("Assets/Exports/candy_corn_3.png").convert_alpha()
candy_corn_img_4 = pygame.image.load\
	("Assets/Exports/candy_corn_4.png").convert_alpha()
candy_corn_images = [candy_corn_img_1, candy_corn_img_2, \
	candy_corn_img_3, candy_corn_img_4]

# Initialize constants and starting conditions
text_font = pygame.font.Font("Assets/NESfont.ttf", 14)
player = Player(pumpkin_images, 212, 384)
candy_corn = Candy(candy_corn_img_1, 224, -32)
clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
frame_counter = 0
score_counter = 0
game = 'ON'

# Play background music (music made by Clint "Volasaurus" Kelly)
pygame.mixer.music.load("Assets/Candy_Corn_Shuffle.wav")
pygame.mixer.music.play(-1)

# Main game loop
while game == 'ON':
	# Quit game if window is closed
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
	
	# Move player left and right
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT] or key[pygame.K_a]:
		if player.x > 32:
			player.x -= 8
		
	elif key[pygame.K_RIGHT] or key[pygame.K_d]:
		if player.x < 384:
			player.x += 8
	
	# Cycle through pumpkin / player animation
	frame_counter += 1
	if frame_counter == 7:
		player.current_image = player.image_list[0]
	
	if frame_counter == 15:
		player.current_image = player.image_list[1]
	
	if frame_counter == 23:
		player.current_image = player.image_list[2]
		
	if frame_counter == 30:
		player.current_image = player.image_list[3]
		frame_counter = 0
	
	# Check for collision beween candy corn and player
	candy_corn.y += 8
	if (((abs((player.x + 32) - candy_corn.x) < 48)) and \
		((abs(player.y - candy_corn.y)) < 8)):
			score_counter += 1
			candy_corn.x = random.randint(32, 384)
			candy_corn.y = -32
			candy_corn.image = candy_corn_images[random.randint(0, 3)]
	
	# If candy corn falls past bottom of screen, return it to the top,
	# with random X position
	if candy_corn.y >= 520:
		candy_corn.x = random.randint(32, 384)
		candy_corn.y = -32
		candy_corn.image = candy_corn_images[random.randint(0, 3)]
		
	# Update score
	score_display = text_font.render("SCORE: " + str(score_counter), True, WHITE)
	
	# Update screen
	screen.blit(starry_night, (0, 0))
	screen.blit(moon_img, (384, 0))
	screen.blit(cloud_img, (-64,100))
	screen.blit(cloud_img, (300, 200))
	screen.blit(candy_corn.image, (candy_corn.x, candy_corn.y))
	screen.blit(score_display, (16,16))
	screen.blit(player.current_image, (player.x, player.y))
	pygame.display.flip()
	clock.tick(FPS)
