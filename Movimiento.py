
from Estructura_Personaje import *

# Ingresar movimiento

juego_1 = Jugador("Juego 2D - Movimiento", 50, 50)
juego_1.iniciar_libreria()
juego_1.poner_titulo()
juego_1.crear_ventana(400, 400)

run = True

while run:

	# Rapidez del jugador
	juego_1.rapidez(60)
	juego_1.rellenar_color()
	juego_1.calcular_movimiento()
	juego_1.movimiento()

	# Dibujar jugador
	juego_1.dibujar_jugador()

	# Cerrar ventana al presionar x
	for evento in pygame.event.get():
		if evento.type ==  pygame.QUIT:
			run = False

		juego_1.presionar_tecla(evento)
		juego_1.despresionar_tecla(evento)

	juego_1.actualizar_ventana()

juego_1.cerrar_ventana()