import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Shape:
    def __init__(self):
        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0
        self.position = [0, 0, -5]
    
    def move(self, direction):
        if direction == 'up':
            self.rotation_x += 5
        elif direction == 'down':
            self.rotation_x -= 5
        elif direction == 'left':
            self.rotation_y += 5
        elif direction == 'right':
            self.rotation_y -= 5
        elif direction == 'front':
            self.position[2] += 0.5
        elif direction == 'back':
            self.position[2] -= 0.5
    
    def draw(self):
        pass

class Cube(Shape):
    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glRotatef(self.rotation_x, 1, 0, 0)
        glRotatef(self.rotation_y, 0, 1, 0)
        glRotatef(self.rotation_z, 0, 0, 1)
        
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        # Back face
        glColor3f(0, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, -1, -1)
        # Top face
        glColor3f(0, 0, 1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 1, -1)
        # Bottom face
        glColor3f(1, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)
        # Right face
        glColor3f(1, 0, 1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        # Left face
        glColor3f(0, 1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, -1)
        glEnd()
        glPopMatrix()

class Cone(Shape):
    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glRotatef(self.rotation_x, 1, 0, 0)
        glRotatef(self.rotation_y, 0, 1, 0)
        glRotatef(self.rotation_z, 0, 0, 1)
        
        glColor3f(0.5, 0.5, 1)
        glutSolidCone(1, 2, 30, 30)
        glPopMatrix()