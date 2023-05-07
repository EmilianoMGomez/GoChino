import pygame
import os
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONUP, QUIT, K_p

WHITE = (255, 255, 255)
BOARDCOLOR = (206, 148, 90)
BLACK = (0, 0, 0)
SHOW_HITBOXES = False

class Prueba():
    def __init__(self,komi=2.5):
            SCREEN_WIDTH = 800
            SCREEN_HEIGHT = 600


            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

            self.move = 0
         
            self.komi = komi
         
         
    def run(self):
        
             
        running=True
        
        while running:
            for event in pygame.event.get():
                self.screen.fill(BOARDCOLOR)
                self.drawGrid()
                
                if event.type == MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                
                
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                   
                elif event.type == QUIT:
                    running = False
                    

            
            pygame.display.update()
         
         
         
         
    def generateSpriteLocations(self):
        locations = []

        for y_index, y_pos in enumerate(range(10, 551, 30)):
            for x_index, x_pos in enumerate(range(10, 551, 30)):
                locations.append([[y_index, x_index], [y_pos, x_pos]])
        
        self.locations = locations
        
        
     #Grafica las lineas del tablero y tambien los circulos en la estrella   
    def drawGrid(self):
        for y_pos in range(10, 551, 30):
            pygame.draw.line(self.screen, BLACK, (10, y_pos), (551, y_pos), width=2)
        
        for x_pos in range(10, 551, 30):
            pygame.draw.line(self.screen, BLACK, (x_pos, 10), (x_pos, 551), width=2)

        star_spots = \
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
        
        for location in star_spots:
            x, y = location
            loc = (x + 1, y)

            pygame.draw.circle(self.screen, BLACK, loc, 5, width=0)    
    
    # indica si mueve el jugador blanco o negr, dependiento del movimiento si es par o impar para poder saber quien mueve
    def passMove(self):
        
        self.move += 1
       
        person = 'Black' if not self.move % 2 else 'White'
               