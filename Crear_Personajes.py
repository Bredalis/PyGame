
import pygame

class Personaje():
	def __init__(self, x, y):
		self.forma = pygame.Rect(0, 0, 20, 20) # Tamaño
		self.forma.center = (x, y) # Ubicar el personaje

	def dibujar(self, ventana):
		pygame.draw.rect(ventana, (0, 255, 0), self.forma)