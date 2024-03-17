
import pygame

class Jugador:
	def __init__(self, titulo, x, y):
		self.titulo = titulo
		self.forma = pygame.Rect(0, 0, 20, 20) # Tamaño
		self.forma.center = (x, y) # Posicion
		self.voltear = False
		
		# Movimientos
		self.mover_arriba = False 
		self.mover_abajo = False 
		self.mover_izquierda = False 
		self.mover_derecha = False

		# Posiciones
		self.reloj = pygame.time.Clock() 

	def iniciar_libreria(self):
		pygame.init()

	def crear_ventana(self, ancho, alto):
		self.ventana = pygame.display.set_mode((ancho, alto))

	def rellenar_color(self):
		self.ventana.fill((0, 0, 20))

	def poner_titulo(self):
		pygame.display.set_caption(self.titulo)

	def dibujar_jugador(self):
		pygame.draw.rect(self.ventana, (0, 255, 0), self.forma)

	def obtener_img(self, url):
		self.img_jugador = pygame.image.load(url)

	def longitud_img(self, num):

		self.ancho = self.img_jugador.get_width()
		self.alto = self.img_jugador.get_height()

		self.img_jugador = pygame.transform.scale(
			self.img_jugador, (self.ancho * num, self.alto * num))		

	def dibujar_animacion(self):
		self.ventana.blit(self.img_jugador, self.forma)

	def calcular_movimiento(self):

		self.delta_x = 0
		self.delta_y = 0

		if self.mover_derecha:
			self.delta_x = 5

		if self.mover_izquierda:
			self.delta_x = -5

		if self.mover_arriba:
			self.delta_y = -5

		if self.mover_abajo:
			self.delta_y = 5

	def movimiento(self):
		self.forma.x = self.forma.x + self.delta_x
		self.forma.y = self.forma.y + self.delta_y

	def movimiento_voltear(self):
		if self.delta_x < 0:
			self.voltear = True

		if self.delta_y > 0:
			self.voltear = False

	def voltear_img(self):
		self.img_volteada = pygame.transform.flip(self.img_jugador, self.voltear, False)
		self.ventana.blit(self.img_volteada, self.forma)

	def rapidez(self, cantidad):
		self.reloj.tick(cantidad)

	def presionar_tecla(self, evento):

		# Si la tecla esta presionada
		
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_a:
				self.mover_izquierda = True

			if evento.key == pygame.K_d:
				self.mover_derecha = True

			if evento.key == pygame.K_w:
				self.mover_arriba = True

			if evento.key == pygame.K_s:
				self.mover_abajo = True

	def despresionar_tecla(self, evento):

		# Si se suelta la tecla
		if evento.type == pygame.KEYUP:
			if evento.key == pygame.K_a:
				self.mover_izquierda = False

			if evento.key == pygame.K_d:
				self.mover_derecha = False

			if evento.key == pygame.K_w:
				self.mover_arriba = False

			if evento.key == pygame.K_s:
				self.mover_abajo = False

	def actualizar_ventana(self):
		pygame.display.update()

	def cerrar_ventana(self):
		pygame.quit()