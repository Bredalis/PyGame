
import pygame

# Iniciar libreria

pygame.init()
pygame.display.set_caption('Juego 2D Con Python')

# Propiedades de la ventana

ancho = 800
alto = 620

# Crear ventana

ventana = pygame.display.set_mode((ancho, alto))

run = True

while run:
	for evento in pygame.event.get():

		# Cerrar la ventana al presionar la x
		if evento.type == pygame.QUIT:
			run = False

pygame.quit()