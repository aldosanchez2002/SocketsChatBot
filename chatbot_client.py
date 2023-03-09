from socket import *
import sys

def main():
    try:
        s = socket(AF_INET, SOCK_STREAM)
    except:
        sys.exit('Error opening socket')

    try:
        s.connect(('localhost', 7069))
    except:
        sys.exit('Error connecting')

    while True:
        if not (bytes_read := s.recv(1024)):
            break
        print(bytes_read.decode())
        s.send(input().encode())
    s.close()

if __name__ == '__main__':
    main()