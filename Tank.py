# Import here
import pygame
import random

pygame.init()

clock = pygame.time.Clock()

# Put Variables here

# Screen
background = pygame.image.load("background.jpeg")
background = pygame.transform.rotozoom(background, 0, 5)
screen = pygame.display.set_mode((600, 800))

# Player
player_surf = pygame.image.load("tank.png")
player_surf = pygame.transform.rotozoom(player_surf, 0, 0.1)
player_rect = player_surf.get_rect(bottomright = (400, 600))



# Game Loop
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(player_surf, player_rect)


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_surf = pygame.image.load("tank_left.png")
            player_surf = pygame.transform.rotozoom(player_surf, 0, 0.1)
            player_rect.x -= 4

        if event.key == pygame.K_RIGHT:
            player_surf = pygame.image.load("tank_right.png")
            player_surf = pygame.transform.rotozoom(player_surf, 0, 0.1)
            player_rect.x += 4

    pygame.display.update()
    clock.tick(60)
