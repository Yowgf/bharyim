import pygame
import sys


screen = pygame.display.set_mode((1366, 768))

purple = (128,0,128)		
pygame.draw.rect(screen, purple, [200,100,50,50])

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
    pygame.display.flip()
