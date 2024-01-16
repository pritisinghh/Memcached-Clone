import socket
from constants import PORT, TYPE

def send_kv_pair(sock, key, value):
    msg = f"set {key} {value}"
    sock.send(msg.encode())
    response = sock.recv(1024).decode()
    print("Received from server: %s" % response)

def get_value(sock, key):
    msg = f"get {key}"
    sock.send(msg.encode())
    response = sock.recv(1024).decode().replace('END' , '')
    print("Received from server: %s" % response)

def start_client():
    # create a socket object
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # get local machine name
    host = socket.gethostname()
    
    port = PORT
    cmd = input("Enter command: ")
    
    # connection to hostname on the port.
    clientsocket.connect((host, port))
    
    
    if cmd.strip().startswith("set"):
        parts = cmd.split(" ")
        key = parts[1]
        value = parts[2]
        send_kv_pair(clientsocket, key, value)

    elif cmd.strip().startswith("get"):
        parts=cmd.split(" ")
        key=parts[1]
        get_value(clientsocket,key)

    clientsocket.close()

if __name__ == "__main__":
    start_client()


