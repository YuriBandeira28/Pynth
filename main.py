import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import funcoes
import tkinter



pygame.init()
display = (980, 720)
window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Defina a perspectiva e a posição da câmera
gluPerspective(45, (display[0] / display[1]), 0.1, 0.0)
glTranslatef(0.0, 0.0, 3)




font = pygame.font.SysFont("Arial", 24)

Quadrados = funcoes.Quadrados
desenhando_circulo = False
desenhando = False
win = tkinter.Tk()
win.geometry("200x200")
win.title("CORES")

Funcoes = funcoes.Funcoes(win)

desenhando_placeholder = False
movendo = False
move_x, move_y = 0,0


while True:
    glLoadIdentity()
    glClearColor(1, 1, 1 ,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    cor = Funcoes.cor

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # clica R para desenhar um quadrado/retangulo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            desenhando = True

        if desenhando:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo pressionado
                desenhando_placeholder = True 
                start_pos = (pygame.mouse.get_pos()[0] / display[0] * 2 - 1,
                             1 - pygame.mouse.get_pos()[1] / display[1] * 2)
                
                start_posX, start_posY = pygame.mouse.get_pos()
                start_posX = start_posX / display[0] * 2 - 1
                start_posY = 1 - start_posY / display[1] * 2

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Botão esquerdo liberado
                desenhando = False
                desenhando_placeholder = False

                end_posX, end_posY = pygame.mouse.get_pos()
                end_posX = end_posX / display[0] * 2 - 1
                end_posY = 1 - end_posY / display[1] * 2

                # print(f"Posição inicial: {(start_posX, start_posY)}, Posição final: {(end_posX, end_posY)}")
                Quadrados.quadrados.append(((start_posX, start_posY), (end_posX, end_posY), cor))
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo pressionado
                movendo = True 
                
                ini_move_x, ini_move_y = pygame.mouse.get_pos()
                ini_move_x = ini_move_x / display[0] * 2 - 1
                ini_move_y = 1 - ini_move_y / display[1] * 2

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Botão esquerdo liberado
                movendo = False

                fim_move_x, fim_move_y = pygame.mouse.get_pos()
                fim_move_x = fim_move_x / display[0] * 2 - 1
                fim_move_y = 1 - fim_move_y / display[1] * 2


    # if desenhando_circulo:
    # if movendo:
    if Funcoes.desenha_3d == True:
        glRotatef(30, 1, 0, 1)
        
    if desenhando_placeholder:
        current_pos = (pygame.mouse.get_pos()[0] / display[0] * 2 - 1,
                       1 - pygame.mouse.get_pos()[1] / display[1] * 2)
        Quadrados.desenha_quadrado(start_pos, current_pos, cor)
    
    
   


    for quadrado in Quadrados.quadrados:
        # glLoadIdentity()
        glPushMatrix()
        Quadrados.desenha_quadrado(quadrado[0], quadrado[1],  quadrado[2])
        glPopMatrix()


    pygame.display.flip()
    pygame.time.wait(10)
    win.update()

    