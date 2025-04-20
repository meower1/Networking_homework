import socket 
import os
import time

def server():

    port= 6969
    ip = '0.0.0.0'
    soc = socket.socket()

    soc.bind((ip,port))

    soc.listen(1)

    c,add= soc.accept()
    print(c,' ', add)

    
        
    data = c.recv(1024).decode()
     
        
    print(f"Received from client: {data}")
            

    response = http_check(data)
    c.sendall(response)
    
    time.sleep(2)

        
    c.close()

def http_check(data):
    try:
        parts = data.split()
        if len(parts) < 3:
            return "HTTP/1.1 400 Bad Request\r\n\r\n"
            
        method, path, version = parts[0], parts[1], parts[2]
        
        if method != 'GET':
            error_html = "<h1>405 Method Not Allowed</h1>"
            return (
                "HTTP/1.1 405 Method Not Allowed\r\n"
                "Allow: GET\r\n"
                f"Content-Length: {len(error_html)}\r\n"
                "Content-Type: text/html\r\n\r\n"
                + error_html
            )
            
        if path == '/moz.html':
            try:
                with open("moz.html", "r", encoding="utf-8") as f:
                    content = f.read()
                body = content.encode("utf-8")
                return (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html\r\n"
                    f"Content-Length: {len(body)}\r\n\r\n"
                ).encode("utf-8") + body
            except FileNotFoundError:
                error_html = "<h1>404 Not Found</h1>"
                return (
                    "HTTP/1.1 404 Not Found\r\n"
                    f"Content-Length: {len(error_html)}\r\n"
                    "Content-Type: text/html\r\n\r\n"
                    + error_html
                ).encode("utf-8")
        else:
            error_html = "<h1>404 Not Found</h1>"
            return (
                "HTTP/1.1 404 Not Found\r\n"
                f"Content-Length: {len(error_html)}\r\n"
                "Content-Type: text/html\r\n\r\n"
                + error_html
            ).encode("utf-8")
            
    except Exception as e:
        error_html = f"<h1>500 Internal Server Error</h1><p>{e}</p>"
        return (
            "HTTP/1.1 500 Internal Server Error\r\n"
            f"Content-Length: {len(error_html)}\r\n"
            "Content-Type: text/html\r\n\r\n"
            + error_html
        ).encode("utf-8")

while True:
    server()

