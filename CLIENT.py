import socket

def request_server(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 9999))
        sock.sendall(data.encode('utf-8'))
        response = sock.recv(1024).decode('utf-8')
        print(f"Otrzymana odpowiedź: {response}")

# Przykładowe żądania
request_server("GET_IP")
request_server("GET_COUNTRIES")
