import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'  # Replace with the IP address where the MT5 is running
port = 8888  # Use the same port number as in the EA script

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server is listening on {host}:{port}")

# Accept a connection
client_socket, addr = server_socket.accept()
print(f"Connection from {addr} has been established.")

# Read the contents of the text file
file_path = "E:\work\data.txt"  # Replace with the actual file path
with open(file_path, 'r') as file:
    file_contents = file.read()

# Send the file contents to the EA
client_socket.sendall(file_contents.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()
