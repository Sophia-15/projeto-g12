import pygame,sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
#Texto sobre next_rect
#next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(615, 15, 170, 60)
# Alterar next_block em game.py após alterar next_rect
next_rect = pygame.Rect(320, 215, 170, 180)

#DEFINE DISPLAY
# Eixos x e y, respectivamente.
screen = pygame.display.set_mode((1350, 690))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT

#SET DA VELOCIDADE DE QUEDA
pygame.time.set_timer(GAME_UPDATE, 200)

# DEFINE BACKGROUND IMG
background_image = pygame.image.load("baterias_background.jpg")
background_rect = background_image.get_rect()
# REDIMENSIONA BACKGROUND IMG PARA O DISPLAY
background_image = pygame.transform.scale(background_image, (1350, 690))
background_rect = background_image.get_rect()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if game.game_over == True:
				game.over()
				sys.exit()
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

	#Drawing
	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	# APLICA A BACKGROUND IMG 
	screen.blit(background_image, background_rect)
	#screen.fill(Colors.dark_blue)

	#screen.blit(score_surface, (365, 20, 50, 50))
	#screen.blit(next_surface, (375, 180, 50, 50))

	#if game.game_over == True:
		#screen.blit(game_over_surface, (320, 450, 50, 50))

	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery))
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	game.draw(screen)

	pygame.display.update()
	clock.tick(60)