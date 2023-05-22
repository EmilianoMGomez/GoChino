
import pygame
import sys

from Clases.prueba import Principal


#variables ventana
ancho_pantalla=800
alto_pantalla=600
color_fondo=(34,121,153) 
size=(ancho_pantalla,alto_pantalla)
clock=pygame.time.Clock() #optimizar las animaciones

#iniciamos pygame
pygame.init() 

#crear ventana
screen=pygame.display.set_mode(size)
screen.fill(color_fondo)

#Titulo
pygame.display.set_caption("Go Chino")

#imagenes de fondo
inicio=pygame.image.load("img/fondo1.png").convert()
width=inicio.get_width()
height=inicio.get_height()
inicio=pygame.transform.scale(inicio,(int(width*1.28),int(height*1.43)))

#Botones de inicio
jugar_contra_pc_img=pygame.image.load("img/pc.png").convert()
jugar_contra_jugador_img=pygame.image.load("img/jugador.png").convert()
salir_img=pygame.image.load("img/salir.png").convert()

class Button():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
    def draw(self):
        action=False
        #posicion del boton
        pos=pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
                print("Clicked")
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        #pintar un boton en ventana
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

#Crear instancias
pc_button=Button(200,150,jugar_contra_pc_img,1)
jugador_button=Button(200,250,jugar_contra_jugador_img,1)
salir_button=Button(200,350,salir_img,1)




#variables juego
en_juego=True
en_inicio=True
en_partida_contra_pc=any
en_partida_contra_jugador=any




while en_juego:
    


    while en_inicio:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()
        screen.blit(inicio,(0,0))
        
        if pc_button.draw():
            en_partida_contra_pc=True
            en_partida_contra_jugador=False
            en_inicio=False
        if jugador_button.draw():
            en_partida_contra_pc=False
            en_partida_contra_jugador=True
            en_inicio=False
        if salir_button.draw():
            sys.exit()        

        pygame.display.flip()
        clock.tick(30)
        
    
    while en_partida_contra_pc:
        en_partida_contra_jugador=False
        en_inicio=True
        en_partida_contra_pc=False
        
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()
        
        
        
        
                
        pygame.display.flip()
    
    
    while en_partida_contra_jugador:
        
        en_partida_contra_jugador=False
        en_inicio=True
        en_partida_contra_pc=False
        
        sc=Principal()
        sc.ejecutar()
        
        
        pygame.display.flip()
        #clock.tick(30)    