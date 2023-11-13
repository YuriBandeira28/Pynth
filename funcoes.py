from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import tkinter

class Quadrados():
    quadrados = []
    def __init__(self):
        pass


    def desenha_quadrado(pos_ini, pos_fim, cor):
        glColor3f(cor[0], cor[1], cor[2])
        glBegin(GL_QUADS)
        glVertex3f(pos_ini[0], pos_ini[1], -1)
        glVertex3f(pos_fim[0], pos_ini[1], -1)
        glVertex3f(pos_fim[0], pos_fim[1], -1)
        glVertex3f(pos_ini[0], pos_fim[1], -1)
        glEnd()


class Funcoes():
    
    def __init__(self, win):
        self.cor = (0, 0, 0) #cor padrão é preto
        self.win = win
        self.desenha_3d = False
        self.botoes()

    
    def define_cor(self, cor):
        self.cor = cor


    def define_3d(self):
        print("chamo")
        self.desenha_3d = True
        # glRotatef(90, 0, 1, 0)
        # glTranslatef(0.0, 0.0, 1)


    def botoes(self):
        #cores
        tkinter.Button(self.win, bg="red",width=2, height=1, command=lambda: self.define_cor((1.0, 0.0, 0.0))).grid(row=1, column=0)
        tkinter.Button(self.win, bg="green",width=2, height=1, command=lambda: self.define_cor((0.0, 1.0, 0.0))).grid(row=1, column=1)
        tkinter.Button(self.win, bg="blue",width=2, height=1, command=lambda: self.define_cor((0.0, 0.0, 1.0))).grid(row=2, column=0)
        tkinter.Button(self.win, bg="yellow",width=2, height=1, command=lambda: self.define_cor((1.0, 1.0, 0.0))).grid(row=2, column=1)
        tkinter.Button(self.win, bg="white",width=2, height=1, command=lambda: self.define_cor((1.0, 1.0, 1.0))).grid(row=3, column=0)
        tkinter.Button(self.win, bg="black",width=2, height=1, command=lambda: self.define_cor((0.0, 0.0, 0.0))).grid(row=3, column=1)

        # define 3d
        tkinter.Button(self.win, text="3D",width=2, height=1, command=self.define_3d).grid(row=5, column=1)
        



# Vermelho: (1.0, 0.0, 0.0) ou (255, 0, 0) - 100% vermelho, 0% verde, 0% azul.
# Verde: (0.0, 1.0, 0.0) ou (0, 255, 0) - 0% vermelho, 100% verde, 0% azul.
# Azul: (0.0, 0.0, 1.0) ou (0, 0, 255) - 0% vermelho, 0% verde, 100% azul.
# Amarelo: (1.0, 1.0, 0.0) ou (255, 255, 0) - 100% vermelho, 100% verde, 0% azul.
# Ciano (Azul claro): (0.0, 1.0, 1.0) ou (0, 255, 255) - 0% vermelho, 100% verde, 100% azul.
# Magenta (Rosa claro): (1.0, 0.0, 1.0) ou (255, 0, 255) - 100% vermelho, 0% verde, 100% azul.
# Branco: (1.0, 1.0, 1.0) ou (255, 255, 255) - 100% vermelho, 100% verde, 100% azul.
# Preto: (0.0, 0.0, 0.0) ou (0, 0, 0) - 0% vermelho, 0% verde, 0% azul.
# Cinza (tons de cinza): Pode ser obtido usando valores RGB iguais, como (0.5, 0.5, 0.5) ou (128, 128, 128) para um cinza médio.