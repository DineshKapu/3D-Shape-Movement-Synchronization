import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from shared.network import NetworkManager
from shared.constants import *
from shared.shapes import Cube, Cone

class MainSystem:
    def __init__(self):
        self.cube = Cube()
        self.cone = Cone()
        self.network = NetworkManager('main')
        self.network.register_handler(self.handle_message)
        
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(1200, 600)
        glutCreateWindow(b"Main System - 3D Shapes Synchronization")
        
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1200/600, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)
        glutIdleFunc(self.display)
    
    def handle_message(self, message, addr):
        if message['type'] == 'cube_move':
            self.cube.rotation_x = message['state']['rotation_x']
            self.cube.rotation_y = message['state']['rotation_y']
            self.cube.rotation_z = message['state']['rotation_z']
            self.cube.position = message['state']['position']
        elif message['type'] == 'cone_move':
            self.cone.rotation_x = message['state']['rotation_x']
            self.cone.rotation_y = message['state']['rotation_y']
            self.cone.rotation_z = message['state']['rotation_z']
            self.cone.position = message['state']['position']
    
    def keyboard(self, key, x, y):
        if key == b'\x1b':  # ESC key
            self.network.stop()
            sys.exit()
    
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Left half - Cube
        glViewport(0, 0, 600, 600)
        glLoadIdentity()
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
        self.cube.draw()
        
        # Right half - Cone
        glViewport(600, 0, 600, 600)
        glLoadIdentity()
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
        self.cone.draw()
        
        glutSwapBuffers()
    
    def run(self):
        glutMainLoop()

if __name__ == "__main__":
    main_system = MainSystem()
    main_system.run()