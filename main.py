import pygame
import sys

# Initialize everything
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
clock.tick(60)

#variaveis
player_x = 250
player_y = 250
player_size = 40

purple = (128,0,128)
rectangle = pygame.Rect(player_x, player_y, player_size, player_size)


# Create the clock to control the frame rate
clock = pygame.time.Clock()

def handle_movement(key):
	x_movement = 0
	y_movement = 0
	step = 1
	if key[pygame.K_UP] or key[pygame.K_w]:
		y_movement -= step
	if key[pygame.K_DOWN] or key[pygame.K_s]:
		y_movement += step
	if key[pygame.K_LEFT] or key[pygame.K_a]:
		x_movement -= step
	if key[pygame.K_RIGHT] or key[pygame.K_d]:
		x_movement += step
	
	rectangle.move_ip(x_movement, y_movement)

def handle_quit():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			break

def handle_keys():
	key = pygame.key.get_pressed()
	handle_movement(key)


running = True
while running:

	# Draw everything
	# First the background
	screen.fill((255, 255, 255))
	# The rectangle
	pygame.draw.rect(screen, purple, rectangle)
	# Then flip the screen!
	pygame.display.flip()

	handle_quit()
	handle_keys()

	clock.tick(200)