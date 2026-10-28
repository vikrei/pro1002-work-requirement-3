import socket

hostname = "localhost"
ip_address = socket.gethostbyname(hostname)

print(f"Hello! The IP address for {hostname} is {ip_address}")