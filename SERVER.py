import socket


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024).decode('utf-8')
        print(f"Odebrano: {request}")
        if request == "GET_IP":
            response = " twój local ip to " + local_ip  # Przykładowy adres IP
        elif request == "GET_COUNTRIES":
            response = "\nPolska\nNiemcy\nFrancja"  # Przykładowa lista krajów
        else:
            response = "Nieznane żądanie"
        sock.sendall(response.encode('utf-8'))


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(5)
    print("Serwer nasłuchuje na porcie 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Połączenie z {addr}")
        handle_client(client_socket)


def get_local_ip():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Use Google's public DNS server to determine the local IP
        # This does not actually create a connection
        s.connect(("8.8.8.8", 80))
        # Get the socket's own address
        ip = s.getsockname()[0]
    finally:
        # Always close the socket after use
        s.close()
    return ip

# Example usage
local_ip = get_local_ip()


start_server()
