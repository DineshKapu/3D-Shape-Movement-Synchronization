import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from shared.network import NetworkManager
from shared.constants import *
from shared.shapes import Cone

class ConeController:
    def __init__(self):
        self.cone = Cone()
        self.network = NetworkManager('cone')
        self.network.register_handler(self.handle_message)
        
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 600)
        glutCreateWindow(b"3D Cone Controller")
        
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 800/600, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)
        glutIdleFunc(self.display)
    
    def handle_message(self, message, addr):
        # Only main system sends messages to cone system
        pass
    
    def keyboard(self, key, x, y):
        key = key.decode('utf-8').lower()
        if key in CONE_KEYS:
            direction = CONE_KEYS[key]
            self.cone.move(direction)
            # Send movement to main system
            self.network.send_message({
                'type': 'cone_move',
                'direction': direction,
                'state': {
                    'rotation_x': self.cone.rotation_x,
                    'rotation_y': self.cone.rotation_y,
                    'rotation_z': self.cone.rotation_z,
                    'position': self.cone.position
                }
            }, MAIN_IP, MAIN_PORT)
        elif key == '\x1b':  # ESC key
            self.network.stop()
            sys.exit()
    
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        self.cone.draw()
        
        glutSwapBuffers()
    
    def run(self):
        glutMainLoop()

if __name__ == "__main__":
    controller = ConeController()
    controller.run()