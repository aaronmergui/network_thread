import socket
import requests
def client():
    try:
        response =requests.get("http://127.0.0.1:5000/port")
        port = int(response.headers['Port-Number'])
        msg=input("enter a message: ")
        udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_client_socket.sendto(msg.encode(), ('localhost', port))
        response, _ = udp_client_socket.recvfrom(1024)
        print( response.decode())
    except requests.RequestException as e:
        print(f'Error connecting to the HTTP server: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    client()