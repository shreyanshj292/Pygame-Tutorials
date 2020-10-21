import pygame
import sys
# print(pygame)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.VIDEORESIZE)
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
white = (255, 255, 255) #red, green, blue
red = (255, 0, 0)
green = (0, 255, 0)
running = True
while running: # game loop
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.VIDEORESIZE)
    pygame.draw.rect(screen, red, (400, 300, 100, 150))
    pygame.draw.circle(screen, green, (400, 300), 26)
    pygame.display.update()

