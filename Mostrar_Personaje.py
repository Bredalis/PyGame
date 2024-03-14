
import pygame
from Crear_Personajes import *

# Iniciar libreria

pygame.init()
pygame.display.set_caption('Juego 2D Con Python')

# Crear personaje

jugador = Personaje(50, 50)

# Propiedades de la ventana

ancho = 800
alto = 620

# Crear ventana

ventana = pygame.display.set_mode((ancho, alto))

run = True

while run:

	# Dibujar personaje
	jugador.dibujar(ventana)

	for evento in pygame.event.get():

		# Cerrar la ventana al presionar la x
		if evento.type == pygame.QUIT:
			run = False

	# Actualizar la pantalla
	pygame.display.update()

pygame.quit()