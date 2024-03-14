
import pygame
from Crear_Personajes import *

# Iniciar libreria

pygame.init()
pygame.display.set_caption('Juego 2D Con Python')

# Crear personaje

jugador = Personaje(50, 50)

# Variables de movimiento 
# para el jugador

mover_arriba = False 
mover_abajo = False 
mover_izquierda = False 
mover_derecha = False 

# Propiedades de la ventana

ancho = 800
alto = 620

# Crear ventana

ventana = pygame.display.set_mode((ancho, alto))

run = True

while run:

	# Calcular movimiento
	# del jugador

	delta_x = 0
	delta_y = 0

	if mover_derecha:
		delta_x = 5

	if mover_izquierda:
		delta_x = -5

	if mover_arriba:
		delta_y = 5

	if mover_abajo:
		delta_y = -5

	# Dibujar personaje
	jugador.dibujar(ventana)

	for evento in pygame.event.get():

		# Cerrar la ventana al presionar la x
		if evento.type == pygame.QUIT:
			run = False

		# Si presiona una tecla
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_a:
				print('Izquierda')

			if evento.key == pygame.K_d:
				print('Derecha')

			if evento.key == pygame.K_w:
				print('Arriba')

			if evento.key == pygame.K_s:
				print('Abajo')

	# Actualizar la pantalla
	pygame.display.update()

pygame.quit()