import socket
import pickle
import threading
from .constants import *

class NetworkManager:
    def __init__(self, role):
        self.role = role
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        if role == 'main':
            self.socket.bind((MAIN_IP, MAIN_PORT))
            self.clients = {}
        elif role == 'cube':
            self.socket.bind((CUBE_IP, CUBE_PORT))
        elif role == 'cone':
            self.socket.bind((CONE_IP, CONE_PORT))
            
        self.running = True
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.daemon = True
        self.receive_thread.start()
    
    def send_message(self, message, target_ip, target_port):
        try:
            data = pickle.dumps(message)
            self.socket.sendto(data, (target_ip, target_port))
        except Exception as e:
            print(f"Error sending message: {e}")
    
    def receive_messages(self):
        while self.running:
            try:
                data, addr = self.socket.recvfrom(4096)
                message = pickle.loads(data)
                if self.message_handler:
                    self.message_handler(message, addr)
            except Exception as e:
                print(f"Error receiving message: {e}")
    
    def register_handler(self, handler):
        self.message_handler = handler
    
    def stop(self):
        self.running = False
        self.socket.close()