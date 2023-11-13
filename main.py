import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import funcoes
import tkinter



pygame.init()
display = (980, 720)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Defina a perspectiva e a posição da câmera
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

font = pygame.font.SysFont("Arial", 24)

Quadrados = funcoes.Quadrados
desenhando_circulo = False
desenhando = False
win = tkinter.Tk()
win.geometry("200x200")
win.title("CORES")

Cores = funcoes.Cores(win)


while True:
    glLoadIdentity()
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    cor = Cores.cor

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


        # clica R para desenhar um quadrado/retangulo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            desenhando = True

      
        if desenhando:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo pressionado
                start_posX, start_posY = pygame.mouse.get_pos()
                start_posX = start_posX / display[0] * 2 - 1
                start_posY = 1 - start_posY / display[1] * 2

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Botão esquerdo liberado
                desenhando = False
                end_posX, end_posY = pygame.mouse.get_pos()
                end_posX = end_posX / display[0] * 2 - 1
                end_posY = 1 - end_posY / display[1] * 2



                print(f"Posição inicial: {(start_posX, start_posY)}, Posição final: {(end_posX, end_posY)}")
                # desenhando_circulo = True
                Quadrados.quadrados.append(((start_posX, start_posY), (end_posX, end_posY), cor))

    # if desenhando_circulo:
    for quadrado in Quadrados.quadrados:
        Quadrados.desenha_quadrado(quadrado[0], quadrado[1],  quadrado[2])

    pygame.display.flip()
    pygame.time.wait(10)
    win.update()

    