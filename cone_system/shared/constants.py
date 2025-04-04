# Network configuration
MAIN_IP = '192.168.1.34'
CUBE_IP = '192.168.1.56'
CONE_IP = '192.168.1.58'
MAIN_PORT = 5000
CUBE_PORT = 5001
CONE_PORT = 5002

# Movement commands
MOVE_UP = 'up'
MOVE_DOWN = 'down'
MOVE_LEFT = 'left'
MOVE_RIGHT = 'right'
MOVE_FRONT = 'front'
MOVE_BACK = 'back'

# Key mappings
CUBE_KEYS = {
    'w': MOVE_UP,
    's': MOVE_DOWN,
    'a': MOVE_LEFT,
    'd': MOVE_RIGHT,
    'q': MOVE_FRONT,
    'e': MOVE_BACK
}

CONE_KEYS = {
    'i': MOVE_UP,
    'k': MOVE_DOWN,
    'j': MOVE_LEFT,
    'l': MOVE_RIGHT,
    'u': MOVE_FRONT,
    'o': MOVE_BACK
}