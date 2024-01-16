# server.py
import socket
import threading
from constants import PORT, TYPE
from time import sleep
from random import random


def handle_client(clientsocket, lock):
    msg = clientsocket.recv(1024).decode()
    parts = msg.split(" ")
    action = parts[0].lower()
    sleep(10)

    response = ""
    if action == "set":
        key = parts[1]
        value = parts[2]
        lock.acquire()
        flag = False
        with open("key_value_pairs.txt", "r") as f:
            sleep(random())
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith(key + ":"):
                    response="NOT STORED"
                    flag = True
            if flag:
                pass 
            else:
                with open("key_value_pairs.txt", "a") as f:
                    f.write(f"{key}:{value}\n")
                    response="STORED" 

        lock.release()

    elif action == "get":
        key = parts[1]
        lock.acquire()
        with open("key_value_pairs.txt", "r") as f:
            sleep(random())
            data = f.readlines()
            for line in data:
                k, v = line.strip().split(":")
                if k == key:
                    response = f"VALUE {key} {len(v)}\r\n{v}\r\nEND\r\n"
                else:
                    response = "KEY NOT FOUND"
        lock.release()
    else:
        response="Invalid"
    
    lock.release
    clientsocket.send(bytes(response , TYPE))
    clientsocket.close()

def start_server():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # get local machine name
    host = socket.gethostname()
    
    port = PORT
    
    # bind to the port
    serversocket.bind((host, port))
    
    # queue up to 5 requests
    serversocket.listen(5)
    
    lock = threading.Lock()
    
    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()
        
        print("Got a connection from %s" % str(addr))
        
        client_thread = threading.Thread(target=handle_client, args=(clientsocket, lock))
        client_thread.start()

if __name__ == "__main__":
    print("Listening ...")
    start_server()

