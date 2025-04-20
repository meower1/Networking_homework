import socket
import time
import os

def client():
    addr= '127.0.0.1'
    port = 6969
    print("mooooooooooz")
    client_socket = socket.socket()
    
    client_socket.connect((addr, port))
   
    message = """GET /moz.html HTTP/1.1
Host: 172.120.124.234:6969
Connection: close\r\n\r\n
"""
    
    client_socket.send(message.encode())
  
    data = client_socket.recv(1024).decode()
   
    print("Received from server: " + data)
    save_html(data)
    
    client_socket.close()


def save_html(data):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "khiar.html")
    print(file_path)
    data= data.split('\r\n')
    print(data[-1])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data[-1])

client()