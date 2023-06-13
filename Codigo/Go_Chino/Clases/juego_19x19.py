import pygame
import os
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONUP, QUIT

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
        self.arreglo_sprites = [[0 for _ in range(19)] for _ in range(19)]

        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

        

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
                    

                    sprites_click = [sprite for sprite in self.sprites if self.colisionSprite(sprite.ubicacion, pos)]

                    if sprites_click and not self.fin_del_juego:
                    
                        sprite_click = sprites_click[0]

                        if not sprite_click.ocupado:
                            self.movimiento += 1
                            color = NEGRO if self.movimiento % 2 else BLANCO

                        

                            x, y = sprite_click.ubicacion
                            ubicacion = (x + 1, y)

                            pygame.draw.circle(self.pantalla, color, ubicacion, 10, 0)

                            sprite_click.ocupado = True
                            sprite_click.color = color
                            
                            

                            if not sprite_click.ocupado:
                                self.movimiento -= 1
                                self.movimiento_blanco = True if not self.movimiento_blanco else False

                            else:
                                self.pasando_en_fila = 0

                                persona = 'Negras' if not self.movimiento % 2 else 'Blancas'
                                pygame.display.set_caption(f'Go Chess | ¡Es el turno de {persona}!')

                    

                elif evento.type == KEYDOWN:
                    if evento.key == K_ESCAPE:
                        ejecutando = False
                        
                

                elif evento.type == QUIT:
                    ejecutando = False
            
            pygame.display.update()
        
        
    def dibujarTablero(self):
        for y_pos in range(10, 551, 30):
            pygame.draw.line(self.pantalla, NEGRO, (10, y_pos), (551, y_pos), width=2)
        
        for x_pos in range(10, 551, 30):
            pygame.draw.line(self.pantalla, NEGRO, (x_pos, 10), (x_pos, 551), width=2)

        posiciones_estrella = \
            [
                (100, 100),
                (100, 280),
                (100, 460),        

                (280, 100),
                (280, 280),
                (280, 460),

                (460, 100),
                (460, 280),
                (460, 460)
            ]
        
        for ubicacion in posiciones_estrella:
            x, y = ubicacion
            loc = (x + 1, y)

            pygame.draw.circle(self.pantalla, NEGRO, loc, 5, width=0)    
        
    
    def dibujarSprites(self):
        for entidad in self.sprites:
            if MOSTRAR_HITBOXES:
                self.pantalla.blit(entidad.surf, entidad.ubicacion)
            if entidad.ocupado:
                x, y = entidad.ubicacion
                ubicacion = (x+1, y)
                pygame.draw.circle(self.pantalla, entidad.color, ubicacion, 10, 0)
    
    
        
    def generarUbicacionesSprites(self):
        ubicaciones = []

        for indice_y, y_pos in enumerate(range(10, 551, 30)):
            for indice_x, x_pos in enumerate(range(10, 551, 30)):
                ubicaciones.append([[indice_y, indice_x], [y_pos, x_pos]])
        
        self.ubicaciones = ubicaciones    
    

    
    def pasarTurno(self):
        self.pasando_en_fila += 1
        if self.pasando_en_fila == 2:
            self.FinPartida()
            return

        self.movimiento += 1
        self.movimiento_blanco = True if not self.movimiento_blanco else False

            
    
    def agregarSprites(self):
        fila = 0
        elemento = 0

        for ubicacion in self.ubicaciones:
            if elemento >= 19:
                fila += 1
                elemento = 0
            if fila > 18:
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
     def FinPartida(self):
        persona_gano = self.calcularQuienGano()
        mensaje_ganador = f'Go Chess | ¡{persona_gano} ha ganado!'

        pygame.display.set_caption(mensaje_ganador)

        self.fin_del_juego = True

    def calcularQuienGano(self):
        puntaje_blanco = self.komi
        puntaje_negro = 0

        blancas_en_tablero, negras_en_tablero = self.encontrarPiezasEnTablero()
        blancas_capturadas, negras_capturadas = self.calcularCasillasRodeadas()

        puntaje_blanco += blancas_en_tablero
        puntaje_negro += negras_en_tablero

        puntaje_blanco += blancas_capturadas
        puntaje_negro += negras_capturadas
        
        print()
        self.imprimir('PUNTAJES FINALES:', 'info')
        self.imprimir(f'{blancas_capturadas=}, {negras_capturadas=}', 'info')
        self.imprimir(f'{blancas_en_tablero=}, {negras_en_tablero=}', 'info')
        self.imprimir(f'{puntaje_blanco=}, {puntaje_negro=}', 'info')
        print()

        if puntaje_blanco > puntaje_negro:
            return 'Blancas'
        else:
            return 'Negras'
    
    def encontrarPiezasEnTablero(self):
        cantidad_blancas = 0
        cantidad_negras = 0

        for fila in self.arreglo_sprites:
            for elemento in fila:
                if not elemento.ocupado:
                    continue

            color = elemento.color

            if color == BLANCO:
                cantidad_blancas += 1
            else:
                cantidad_negras += 1

        return (cantidad_blancas, cantidad_negras)

    def calcularCasillasRodeadas(self):
        cantidad_blancas = 0
        cantidad_negras = 0
    
        self.grupos_vacios = []
        self.cuentas_vacias = []
        self.colores_vacios = []

        self.visitados = []        

        for y, fila in enumerate(self.arreglo_sprites):
            for x, sprite in enumerate(fila):
                if sprite.ocupado:
                    continue
            
                self.encontrarCasillasVacias(y, x)

        for indice in range(len(self.colores_vacios)):
            cuenta_vacia = self.cuentas_vacias[indice]
            colores_vacios = self.colores_vacios[indice]

            if NEGRO not in colores_vacios and BLANCO in colores_vacios:
                cantidad_blancas += cuenta_vacia
            if BLANCO not in colores_vacios and NEGRO in colores_vacios:
                cantidad_negras += cuenta_vacia
    
        return (cantidad_blancas, cantidad_negras)