
### Server code by Soumik Das...

import socket
import threading

# Server to handle incoming connections
def handle_client(client_socket, client_address):
    print(f"New connection: {client_address}")

    # Handle communication with the client
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Message from {client_address}: {message}")
            
            # Broadcast the message to all connected clients
            broadcast_message(message, client_socket)
        except:
            break

    client_socket.close()

# Function to broadcast messages to all clients
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                clients.remove(client)

# Server setup
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))  # Listen on port 12345
    server.listen(5)
    print("Server started. Waiting for connections...")

    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# List of clients
clients = []

# Start the server
if __name__ == "__main__":
    start_server()
