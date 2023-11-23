import os
import pygame
import sys

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()

info = pygame.display.Info()
monitor_size = [pygame.display.Info().current_w,
                pygame.display.Info().current_h]

screen = pygame.display.set_mode((monitor_size), pygame.RESIZABLE)
clock = pygame.time.Clock()

def show_resting_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if cont == 0:
                        cont = 25
                    else:
                        cont -= 1

        # DEFINE BACKGROUND IMG
        background_image = pygame.image.load(r"C:\Users\gmam_cesar\Downloads\python\PROJ\projeto-g12\src\menu\assets\resting.png")
        background_rect = background_image.get_rect()
        # REDIMENSIONA BACKGROUND IMG PARA O DISPLAY
        background_image = pygame.transform.scale(background_image, monitor_size)
        screen.blit(background_image, background_rect)
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

show_resting_screen()