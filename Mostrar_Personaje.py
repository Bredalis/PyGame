
from Estructura_Personaje import *

# Mostrar personaje

juego_1 = Jugador("Juego 2D - Mostrar Personajes", 50, 50)
juego_1.iniciar_libreria()
juego_1.poner_titulo()
juego_1.crear_ventana(800, 620)

run = True

while run:

	# Dibujar jugador

	juego_1.dibujar_jugador()

	# Cerrar ventana al presionar x
	
	for evento in pygame.event.get():
		if evento.type ==  pygame.QUIT:
			run = False

	juego_1.actualizar_ventana()

juego_1.cerrar_ventana()