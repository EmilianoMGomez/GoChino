import pygame
import subprocess

pygame.init()

# Definimos algunos colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# Definimos la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Definimos la fuente para el texto
fuente = pygame.font.Font(None, 50)

# Definimos los rectángulos para cada opción del menú
rectangulo_1vs1 = pygame.Rect(ANCHO_PANTALLA/2 - 100, 200, 200, 50)
rectangulo_1vsPC = pygame.Rect(ANCHO_PANTALLA/2 - 100, 300, 200, 50)
rectangulo_salir = pygame.Rect(ANCHO_PANTALLA/2 - 100, 400, 200, 50)

# Definimos el rectángulo para el fondo
rectangulo_fondo = pygame.Rect(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)

# Loop principal del juego
while True:
    # Manejador de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Si se hace clic en el rectángulo 1vs1, se muestra el mensaje correspondiente
            if rectangulo_1vs1.collidepoint(evento.pos):
                print("Has seleccionado jugar 1vs1")
                pygame.quit()
               
                # Aquí puedes llamar a la función correspondiente para jugar 1vs1
                
                subprocess.run(["python3","/home/emiliano/Escritorio/GoChino/Codigo/ejemplo.py"])
                    
                 
                 
            # Si se hace clic en el rectángulo 1vsPC, se muestra el mensaje correspondiente
            if rectangulo_1vsPC.collidepoint(evento.pos):
                print("Has seleccionado jugar 1vsPC")
                # Aquí puedes llamar a la función correspondiente para jugar 1vsPC
            if rectangulo_salir.collidepoint(evento.pos):
                print("Has seleccionado salir del juego")
                pygame.quit()
                sys.exit()

    # Dibujamos el fondo y los rectángulos para cada opción del menú
    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, NEGRO, rectangulo_1vs1)
    pygame.draw.rect(pantalla, NEGRO, rectangulo_1vsPC)
    pygame.draw.rect(pantalla, NEGRO, rectangulo_salir)
    pygame.draw.rect(pantalla, AZUL, rectangulo_fondo)

    # Añadimos el texto a cada rectángulo
    texto_1vs1 = fuente.render("Jugar 1vs1", True, BLANCO)
    pantalla.blit(texto_1vs1, (rectangulo_1vs1.x + 20, rectangulo_1vs1.y + 10))

    texto_1vsPC = fuente.render("Jugar 1vsPC", True, BLANCO)
    pantalla.blit(texto_1vsPC, (rectangulo_1vsPC.x + 20, rectangulo_1vsPC.y + 10))

    # Añadimos el texto para la opción de salida
    texto_salir = fuente.render("Salir", True, BLANCO)
    pantalla.blit(texto_salir, (ANCHO_PANTALLA/2 - 35, 400))
    # Actualizamos la pantalla
    pygame.display.flip()

