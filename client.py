import socket, sys

def create_tcp_socket():
    print("Creating socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        sys.exit()
        print("error creating socket")
    print("socket succesfully created")
    return s


def get_remote_ip(host):
    print("getting IP for " +host)
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("error getting ip")
        sys.exit()
    print("Ip of " +host+ " is " +remote_ip)
    return remote_ip

def send_data(s, payload):
    try:
        s.sendall(payload.encode())
    except socket.error:
        sys.exit()
            
def main():
    try:
        host = 'www.google.com'
        port = 80
        payload = 'GET / HTTP/1.0\r\nHOST: ' + host + '\r\n\r\n'
        buffer_size = 4096
        
        s = create_tcp_socket()
        
        remote_ip = get_remote_ip(host)
        
        s.connect((remote_ip,port))
        print("Socket Connected to " +host+ " on ip "+remote_ip)
        
        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)
        
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e :
        print(e)
    finally:
        s.close()
        
if __name__ == "__main__":
    main()