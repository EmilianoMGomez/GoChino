import pygame
# constantes para eventos, teclas y botones del mouse.
from pygame.locals import MOUSEBUTTONDOWN,MOUSEBUTTONUP, QUIT,K_ESCAPE, KEYDOWN, K_p
import numpy as np
import time
import random

# colores
Negro = (0, 0, 0)
Blanco = (255,255,255)
#color del tablero
ColorTablero = (0,51,25)
sp= 32
alt=589

class Punto(pygame.sprite.Sprite):
    def __init__(self, array_indexes, location, size, color):
        super(Punto, self).__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.location = location
        self.array_indexes = array_indexes
        self.occupied = False
        self.color = None


def obtenerVecinos(y, x, board_shape): 
    vecinos = list()

    if y > 0:
        vecinos.append((y - 1, x))
    if y < board_shape[0] - 1:
        vecinos.append((y + 1, x))
    if x > 0:
        vecinos.append((y, x - 1))
    if x < board_shape[1] - 1:
        vecinos.append((y, x + 1))

   
    return vecinos

def colisionSprite(posicion_sprite, posicion_click):
    sprite_y, sprite_x = posicion_sprite
    click_y, click_x = posicion_click

    if sprite_y - 10 < click_y < sprite_y + 10:
        if sprite_x - 10 < click_x < sprite_x + 10:
            return True

    return False


class Principal:
    def __init__(self):
        self.locations = None
        self.visited = None
        self.empty_colors = None
        self.empty_counts = None
        self.empty_groups = None
        self.gameover = None
        self.passed_in_a_row = None
        self.komi = None
        self.turno_blanco = None
        self.turno = None
        self.screen = None
        self.sprite_array = None
        self.sprites = None
    def init(self, komi=2.5):
        
        pygame.init()
        #Dimensiones de la pantalla
        anchoDePantalla = 620
        altoDePantalla = 690

        # Asignamos un objeto de Sprites
        self.sprites = pygame.sprite.Group()
       

        self.sprite_array = [[0 for _ in range(19)] for _ in range(19)]
     
        self.screen = pygame.display.set_mode((anchoDePantalla, altoDePantalla))

        #La siguiente linea indica el turno de cada jugador
        pygame.display.set_caption('GO Chino! | Jugando')
        

        # contador de turnos
        self.turno = 0
        # turno jugador blanco
        self.turno_blanco = False
        # Ventaja del jugador que comienza segundo
        self.komi = komi
        self.passed_in_a_row = 0
        self.gameover = False


    def iniciarVSbot(self):
        clock = pygame.time.Clock()
        fps = 30
        # Generamos las ubicaciones de los Sprites
        self.ubicacionSprites()
        # Ubicamos los Sprites
        self.ubicarSprites()
        ejecutando = True
        
       
        ubicacionTurno = self.screen.get_width() - 500
        
        # Creamos el fondo de la pantalla
        self.screen.fill(ColorTablero)
        
        self.dibujarTablero()
       
        bot = 0
        cont = 0
        contbot= 0
        while ejecutando:
            clock.tick(fps)
            
            if self.gameover:
                ejecutando = False
                if self.calcularQuienGano() == 'White':
                    # llamar a pantalla de ganador con ganador blanco
                    self.ganador("blanco")
                else:
                    # llamar a pantalla de ganador con ganador negro
                    self.ganador("negro")

            if self.turno % 2 == 0:
                cont=0
                for event in pygame.event.get():

                    self.dibujarSprites()

                    if event.type == MOUSEBUTTONDOWN:
                       
                        pos = pygame.mouse.get_pos()

                        
                        clicked_sprites = [sprite for sprite in self.sprites if colisionSprite(sprite.location, pos)]
                        
                       
                        if clicked_sprites:
                            
                            
                            clicked_sprite = clicked_sprites[0]
                            #verificar si el sprite clikeado no está ocupado.
                            if not clicked_sprite.occupied:
                                self.turno += 1
                                # colorcirculo es negro si el numero es impar y blanco si es par
                                colorCirculo = Negro if self.turno % 2 else Blanco

                                
                                x, y = clicked_sprite.location
                                posicion = (x + 1, y)

                              

                                clicked_sprite.occupied = True
                                clicked_sprite.color = colorCirculo

                                # Envia a la funcion el Sprite clickeado
                                self.capturePieces(*clicked_sprite.array_indexes)

                                if not clicked_sprite.occupied:
                                    self.turno -= 1
                                    self.turno_blanco = True if not self.turno_blanco else False

                                else:
                                    self.passed_in_a_row = 0
                                    fichas = self.calcularFichas()
                                    print("se calcula")
                                    

                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            ejecutando = False

                        elif event.key == K_p:
                            player = 'White' if not self.turno % 2 else 'Black'
                            self.pasarTurno()
                    elif event.type == QUIT:
                        ejecutando = False

                    self.screen.fill(ColorTablero)
                    
                    self.dibujarTablero()
                    self.dibujarSprites()
                    
                    contbot=0
            else:
                
                if contbot == 0:
                    contbot = 1
                    pygame.time.delay(1000)
                if self.passed_in_a_row==1:
                    if self.calcularQuienGano()=="White":
                        self.pasarTurno()


                listiña=[]
                self.screen.fill(ColorTablero)
                
                self.dibujarTablero()
                self.dibujarSprites()
                
                for sprite in self.sprites:
                    if sprite.occupied and sprite.color == Negro:
                        
                        for loc in self.locations:
                            if sprite.location==loc[1]:
                                vecinos = obtenerVecinos(loc[0][1],loc[0][0], (19, 19))
                                for vec in vecinos:
                                    spritiño = self.sprite_array[vec[0]][vec[1]]
                                    if not spritiño.occupied:
                                        listiña.append(spritiño.location)

                if 0 == 0:
                    pos= random.choice(listiña)
                    cont = cont + 1
                    print("contador")
                    print(cont)
                    if cont == 200:
                        self.pasarTurno()
                    
                    clicked_sprites = [sprite for sprite in self.sprites if colisionSprite(sprite.location, pos)]
                    # asegurarse de que se ha hecho clic en al menos un sprite
                    if clicked_sprites:
                            clicked_sprite = clicked_sprites[0]
                            # verificar si el sprite clikeado no está ocupado.
                            if not clicked_sprite.occupied:
                                self.turno += 1
                                # colorcirculo es negro si el numero es impar y blanco si es par
                                colorCirculo = Negro if self.turno % 2 else Blanco

                                # obtener las coordenadas x , y de la ubicación del sprite clikeado.
                                x, y = clicked_sprite.location
                                posicion = (x + 1, y)

                                
                                clicked_sprite.occupied = True
                                clicked_sprite.color = colorCirculo

                                # Envia a la funcion el Sprite clickeado
                                self.capturePieces(*clicked_sprite.array_indexes)

                                if not clicked_sprite.occupied:
                                    self.turno -= 1
                                    self.turno_blanco = True if not self.turno_blanco else False

                                else:
                                    self.passed_in_a_row = 0

                                    fichas = self.calcularFichas()
                                    print("se calcula")
                                    


            pygame.display.update()
        pygame.quit()


    def pasarTurno(self):
        self.passed_in_a_row += 1
        if self.passed_in_a_row == 2:
            self.FinPartida()
            return

        self.turno += 1
        self.turno_blanco = True if not self.turno_blanco else False

        jugador = 'NEGRO' if not self.turno % 2 else 'BLANCO'
        pygame.display.set_caption(f'Go Chino! | ')

    #llama a la pantalla de final del juego
    def FinPartida(self):
        jugadorGanador = self.calcularQuienGano()
        self.gameover = True

    #retortna blanco o negro
    def calcularQuienGano(self):
        white_score = self.komi
        black_score = 0

        white_on_board, black_on_board = self.encontrarPiezasEnTablero()
        white_surrounded, black_surrounded = self.calcularCasillasRodeadas()

        white_score += white_on_board
        black_score += black_on_board

        white_score += white_surrounded
        black_score += black_surrounded

        if white_score > black_score:
            return 'White'
        else:
            return 'Black'

    def calcularFichas(self):
        list=[]
        white_score = self.komi
        black_score = 0

        white_on_board, black_on_board = self.encontrarPiezasEnTablero()
        white_surrounded, black_surrounded = self.calcularCasillasRodeadas()

        white_score += white_on_board
        black_score += black_on_board

        white_score += white_surrounded
        black_score += black_surrounded
        list.append(white_score)
        list.append(black_score)
        return list

    def ganador(self, color):
        pygame.init()
        screen = pygame.display.set_mode((700, 600))
       
        if color == "blanco":
            background_image = pygame.image.load("img/ganaron_blanca.jpg").convert()
        elif color == "negro":
            background_image = pygame.image.load("img/ganaron_negras.jpg").convert()
        else:
            # Color no válido, salir sin mostrar imagen
            return

        background_image = pygame.transform.scale(background_image, (700, 600))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                

            screen.blit(background_image, (0, 0))        
            pygame.display.flip()
            

    def encontrarPiezasEnTablero(self):
        white_count = 0
        black_count = 0

        for row in self.sprite_array:
            for item in row:
                if not item.occupied:
                    continue

                color = item.color

                if color == Blanco:
                    white_count += 1
                else:
                    black_count += 1

        return white_count, black_count

    #retorna espacio "cercado"
    def calcularCasillasRodeadas(self):
        white_count = 0
        black_count = 0

        self.empty_groups = []
        self.empty_counts = []
        self.empty_colors = []
        self.visited = []

        for y, row in enumerate(self.sprite_array):
            for x, sprite in enumerate(row):
                if sprite.occupied:
                    continue

                self.encontrarCasillasVacias(y, x)

        for index in range(len(self.empty_colors)):
            empty_count = self.empty_counts[index]
            empty_colors = self.empty_colors[index]

            if Negro not in empty_colors and Blanco in empty_colors:
                white_count += empty_count
            if Blanco not in empty_colors and Negro in empty_colors:
                black_count += empty_count

        return white_count, black_count

   
    def encontrarCasillasVacias(self, y, x, agregando=False):
        if not agregando:
            self.empty_groups.append([])
            self.empty_counts.append(0)
            self.empty_colors.append([])

        vecinos =obtenerVecinos(y, x, (19, 19))
        vecinos.append((y, x))

        for location in vecinos:
            sprite = self.sprite_array[location[0]][location[1]]
            if sprite.occupied or sprite in self.visited:
                continue

            self.visited.append(sprite)
            self.empty_groups[-1].append(location)
            self.empty_counts[-1] += 1
            self.empty_colors[-1] += self.obtenerColoresNoVaciosDeVecinos(y, x)
            self.encontrarCasillasVacias(location[0], location[1], agregando=True)

    #devuelve el color de la ubicacion ocupada
    def obtenerColoresNoVaciosDeVecinos(self, y, x):
        colors = []

        vecinos = obtenerVecinos(y, x, (19, 19))
        for location in vecinos:
            sprite = self.sprite_array[location[0]][location[1]]
            if not sprite.occupied:
                continue
            colors.append(sprite.color)

        return colors

    
    def probarGrupo(self, board, opponent_board, y, x, current_group):

        pos = (y, x)

        if current_group[pos]:
            # las fichas ya testeads no son liberates
            return False

        #verifica si hay una ficha del rival en pos
        if opponent_board[pos]:
            current_group[pos] = True

            vecinos = obtenerVecinos(y, x, board.shape)


            for yn, xn in vecinos:
                has_liberties = self.probarGrupo(board, opponent_board, yn, xn, current_group)
                if has_liberties:
                    return True
            return False

        return not board[pos]

    def capturePieces(self, y, x):
       
        # Tablero auxiliar blanco
        tablero_blanco = np.array(
            [[1.0 if item.color == Blanco and item.occupied else 0.0 for item in row] for row in self.sprite_array],
            dtype=int)
        # Tablero auxiliar negro
        tablero_negro = np.array(
            [[1.0 if item.color == Negro and item.occupied else 0.0 for item in row] for row in self.sprite_array],
            dtype=int)

        # cambiamos el turno
        turno_blanco = self.turno_blanco
        self.turno_blanco = True if not self.turno_blanco else False

        # Llamamos a la funcion enviandole los dos tableros
        tablero_resultante = self.fastCapturePieces(tablero_negro, tablero_blanco, turno_blanco, y, x)

        for index1, row in enumerate(tablero_resultante):
            for index2, item in enumerate(row):
                
                color = Blanco if item == 1 else Negro
               
                occupied = True if item != 0 else False

                
                self.sprite_array[index1][index2].occupied = occupied
                self.sprite_array[index1][index2].color = color

    def fastCapturePieces(self, black_board_, white_board_, turn_white, y, x):

        black_board, white_board = black_board_.copy(), white_board_.copy()

        
        vecinos = obtenerVecinos(y, x, black_board.shape)
       
        board = white_board if turn_white else black_board
        opponent_board = black_board if turn_white else white_board
        #crea otra copia del tablero del rival
        original_opponent_board = opponent_board.copy()

        # testear movimientos suicida
        original_pos = (y, x)

        original_pos = original_pos[::-1]

        #array 19x19 tipo booleano
        current_group = np.zeros((19, 19), dtype=bool)
        original_pos_has_liberties = self.probarGrupo(opponent_board, board, *original_pos, current_group)


        
        for pos in vecinos:
            
            pos = pos[::-1]

            if not opponent_board[pos]:
                continue
            #el código crea una matriz booleana de tamaño 19x19 llena de False
            current_group = np.zeros((19, 19), dtype=bool)
            has_liberties = self.probarGrupo(board, opponent_board, *pos, current_group)

            if not has_liberties:
                opponent_board[current_group] = False

        same = True
        break_out = False

        for row_index, row in enumerate(original_opponent_board):
            for item_index, item in enumerate(row):
                if opponent_board[row_index, item_index] != item:
                    same = False
                    break_out = True
                    break
            if break_out:
                break

        out_board = [[i for i in range(19)] for v in range(19)]
        for i in range(19):
            for v in range(19):
                if white_board[i][v]:
                    out_board[i][v] = 1
                elif black_board[i][v]:
                    out_board[i][v] = -1
                else:
                    out_board[i][v] = 0

        if same and not original_pos_has_liberties:
            out_board[original_pos[0]][original_pos[1]] = 0

            return out_board
        else:
            return out_board

    def ubicacionSprites(self):
        ubicaciones = []


        for y_index, y_pos in enumerate(range(10, alt, sp)):
            for x_index, x_pos in enumerate(range(10, alt, sp)):
                ubicaciones.append([[y_index, x_index], [y_pos, x_pos]])

        # se guarda la lista en la variable de clase
        self.locations = ubicaciones

   
    def ubicarSprites(self):
        # rastrear la fila y el índice del elemento en la matriz
        fila = 0
        item = 0

        # iterar a través de las ubicaciones generadas
        for location in self.locations:

            if item >= 19:
                fila += 1
                item = 0
            if fila > 18:
                break

            sprite = Punto(*location, (10, 10), (255, 32, 1))

            # el sprite recién creado se agrega al grupo de sprites
            self.sprites.add(sprite)

            # también se agrega a la matriz
            self.sprite_array[item][fila] = sprite


            # siguiente elemento
            item += 1

    # Metodo para Dibujar lineas del tablero
    def dibujarTablero(self):

        for y_pos in range(10, alt,sp):
            pygame.draw.line(self.screen, Negro, (10, y_pos), (alt, y_pos), width=2)
        for x_pos in range(10, alt, sp):
            pygame.draw.line(self.screen, Negro, (x_pos, 10), (x_pos, alt), width=2)

    #dibuja la ficha en el lugar seleccionado
    def dibujarSprites(self):

        for entity in self.sprites:
            if entity.occupied:
                x, y = entity.location
                loc = (x+1,y)
                pygame.draw.circle(self.screen, entity.color, loc, 10, 0)
               



    