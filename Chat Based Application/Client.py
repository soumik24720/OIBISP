### Client code by Soumik Das...

import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"New message: {message}")
        except:
            print("Connection lost.")
            break

# Client setup
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))  # Connect to the server on localhost, port 12345

    # Start receiving messages in a separate thread
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input("Enter your message: ")
        if message.lower() == 'exit':
            break
        client.send(message.encode("utf-8"))

    client.close()

# Start the client
if __name__ == "__main__":
    start_client()
