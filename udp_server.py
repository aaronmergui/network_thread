import threading
import socket
def udp_server(port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('127.0.0.1', port))

    while True:
        data, addr = udp_socket.recvfrom(1024)
        message = data.decode()

        # Check the received code and send the appropriate response
        if message == "Cyber Himmelfarb":
            response = "Victory!"
        else:
            response = "No Entry"

        udp_socket.sendto(response.encode(), addr)

