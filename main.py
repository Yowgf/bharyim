import pygame

# TODO: put this initialization stuff in their own functions

# Initialize everything
pygame.init()
screen_width = 500
screen_height = 500
fps = 60
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Initialize floor
floor_height = 50
red = (255, 0, 0)
floor_rectangle = pygame.Rect(0, screen_height - floor_height, screen_width, floor_height)

# Initialize player
player_size = 40
player_x = 250
player_y = screen_height - floor_height - player_size

purple = (128,0,128)
rectangle = pygame.Rect(player_x, player_y, player_size, player_size)

# TODO: put this jump stuff somewhere else (it is not good to have global variables)
jump_speed_max = 15
jump_speed_min = -jump_speed_max
jump_speed = jump_speed_max
isJumping = False

jump_delay = 500 # In milliseconds
last_jumped_at = 0

# Create the clock to control the frame rate
clock = pygame.time.Clock()

def handle_movement(key):
	x_movement = 0
	y_movement = 0
	walk_speed = 3

	# Walk movement
	if key[pygame.K_LEFT] or key[pygame.K_a]:
		x_movement -= walk_speed
	if key[pygame.K_RIGHT] or key[pygame.K_d]:
		x_movement += walk_speed
	
	# Jump movement. Object (e.g. player) goes up until jump_speed is 0. When
	# jump_speed becomes negative, the player starts going down.
	global isJumping
	global jump_speed
	global last_jumped_at
	global jump_delay
	current_time = pygame.time.get_ticks()
	if isJumping is False and key[pygame.K_SPACE] and current_time > last_jumped_at + jump_delay:
		isJumping = True
		last_jumped_at = current_time
	if isJumping:
		y_movement -= jump_speed
		jump_speed -= 1
	if jump_speed < jump_speed_min:
		isJumping = False
		jump_speed = jump_speed_max
	
	# Process the movement changes
	rectangle.move_ip(x_movement, y_movement)

# Returns True if program is to keep running, or False otherwise.
def handle_quit():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			return running
	return True

def handle_keys():
	key = pygame.key.get_pressed()
	handle_movement(key)


running = True
while running:
	clock.tick(fps)
	running = handle_quit()
	if running == False:
		break

	# Draw everything
	# First the background
	screen.fill((0, 0, 0))

	# TODO: create function `draw` to encapsulate this behavior
	# Draw everything
	pygame.draw.rect(screen, red, floor_rectangle)
	pygame.draw.rect(screen, purple, rectangle)

	# Then flip the screen!
	pygame.display.flip()

	handle_keys()
