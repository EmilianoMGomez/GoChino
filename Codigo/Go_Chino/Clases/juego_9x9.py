import pygame
import os
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONUP, QUIT, K_p
import numpy as np

BLANCO = (255, 255, 255)
COLORTABLERO = (206, 148, 90)
NEGRO = (0, 0, 0)
MOSTRAR_HITBOXES = False

class Punto(pygame.sprite.Sprite):
    def __init__(self, indices_array, ubicacion, tamaño, color):
        super(Punto, self).__init__()
        self.surf = pygame.Surface(tamaño)
        self.surf.fill(color)

        self.ubicacion = ubicacion
        self.indices_array = indices_array
        self.ocupado = False
        self.color = None



class Principal():     
    def __init__(self, komi=2.5):
        pygame.init()

        ANCHO_PANTALLA = 600
        ALTO_PANTALLA = 600

        self.sprites = pygame.sprite.Group()
        self.arreglo_sprites = [[0 for _ in range(9)] for _ in range(9)]

        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

        #pygame.display.set_caption('Go Chess | ¡Es el turno de las negras!')
        #pygame.display.set_allow_screensaver(True)

        #if os.path.exists('./iconFile.png'):
        #   pygame.display.set_icon(pygame.image.load('./iconFile.png'))

        self.movimiento = 0
        self.movimiento_blanco = False

        self.pasando_en_fila = 0
        self.fin_del_juego = False
        
        self.komi = komi        
            
            
    def ejecutar(self):
        
        self.generarUbicacionesSprites()
        self.agregarSprites()

        ejecutando = True

        while ejecutando:
            for evento in pygame.event.get():
                self.pantalla.fill(COLORTABLERO)

                self.dibujarTablero()
                self.dibujarSprites()

                if evento.type == MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    #self.imprimir(f'Posición clickeada: {pos}', 'info')

                    sprites_click = [sprite for sprite in self.sprites if self.colisionSprite(sprite.ubicacion, pos)]

                    if sprites_click and not self.fin_del_juego:
                    #   self.imprimir('Sprite detectado.', 'info')
                        sprite_click = sprites_click[0]

                        if not sprite_click.ocupado:
                            self.movimiento += 1
                            color = NEGRO if self.movimiento % 2 else BLANCO

                        #  self.imprimir(f'Ubicación del sprite click: {sprite_click.ubicacion}', 'info')

                            x, y = sprite_click.ubicacion
                            ubicacion = (x + 1, y)

                            pygame.draw.circle(self.pantalla, color, ubicacion, 10, 0)

                            sprite_click.ocupado = True
                            sprite_click.color = color
                            
                            # self.capturarPiezas(*sprite_click.indices_array)

                            if not sprite_click.ocupado:
                                self.movimiento -= 1
                                self.movimiento_blanco = True if not self.movimiento_blanco else False

                            else:
                                self.pasando_en_fila = 0

                                persona = 'Negras' if not self.movimiento % 2 else 'Blancas'
                                pygame.display.set_caption(f'Go Chess | ¡Es el turno de {persona}!')

                    #else:
                        #self.imprimir('No se detectó ningún sprite.', 'info')

                    #print()

                elif evento.type == KEYDOWN:
                    if evento.key == K_ESCAPE:
                        ejecutando = False
                        
                    elif evento.key == K_p:
                        jugador = 'Blancas' if not self.movimiento % 2 else 'Negras'

                        self.imprimir(f'{jugador} ha pasado su turno.', 'info')
                        self.pasarTurno()

                elif evento.type == QUIT:
                    ejecutando = False
            
            pygame.display.update()
        
        #pygame.quit()       
        
        
      
    
    
    def dibujarTablero(self):
        for y_pos in range(55, 500, 55):
            pygame.draw.line(self.pantalla, NEGRO, (55, y_pos), (500, y_pos), width=2)

        for x_pos in range(55, 500, 55):
            pygame.draw.line(self.pantalla, NEGRO, (x_pos, 55), (x_pos, 500), width=2)

        # posiciones_estrella = [
        #     (70, 70),
        #     (140, 70),
        #     (210, 70),

        #     (70, 140),
        #     (140, 140),
        #     (210, 140),

        #     (70, 210),
        #     (140, 210),
        #     (210, 210)
        # ]

        # for ubicacion in posiciones_estrella:
        #     x, y = ubicacion
        #     loc = (x + 1, y + 1)

        #     pygame.draw.circle(self.pantalla, NEGRO, loc, 5, width=0)

        
    
    def dibujarSprites(self):
        for entidad in self.sprites:
            if MOSTRAR_HITBOXES:
                self.pantalla.blit(entidad.surf, entidad.ubicacion)
            if entidad.ocupado:
                x, y = entidad.ubicacion
                ubicacion = (x+1, y)
                pygame.draw.circle(self.pantalla, entidad.color, ubicacion, 15, 0)
    
    
        
    def generarUbicacionesSprites(self):
        ubicaciones = []

        for indice_y, y_pos in enumerate(range(55, 500, 55)):
            for indice_x, x_pos in enumerate(range(55, 500, 55)):
                ubicaciones.append([[indice_y, indice_x], [y_pos, x_pos]])
        
        self.ubicaciones = ubicaciones    
    

    
    def pasarTurno(self):
        self.pasando_en_fila += 1
        if self.pasando_en_fila == 2:
            self.FinPartida()
            return

        self.movimiento += 1
        self.movimiento_blanco = True if not self.movimiento_blanco else False

        persona = 'Negras' if not self.movimiento % 2 else 'Blancas'
        #pygame.display.set_caption(f'Go Chess | ¡Es el turno de {persona}!')
    
    
    def agregarSprites(self):
        fila = 0
        elemento = 0

        for ubicacion in self.ubicaciones:
            if elemento >= 9:
                fila += 1
                elemento = 0
            if fila > 8:
                break
            
            sprite = Punto(*ubicacion,(10,10),(255, 32, 1))
            self.sprites.add(sprite)
            self.arreglo_sprites[elemento][fila] = sprite

            elemento += 1
         
        
    def colisionSprite(self, ubicacion_sprite, ubicacion_clic):
        sprite_y, sprite_x = ubicacion_sprite
        clic_y, clic_x = ubicacion_clic

        if sprite_y - 10 < clic_y < sprite_y + 10:
            if sprite_x - 10 < clic_x < sprite_x + 10:
                return True
        
        return False 
     
              