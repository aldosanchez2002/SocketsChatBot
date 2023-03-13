from socket import *
import sys, datetime, time, _thread

lock = _thread.allocate_lock()

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
        exit_thread = [False]
        timer_thread = _thread.start_new_thread(timer, (exit_thread,))
        if not (bytes_read := s.recv(1024)):
            break
        exit_thread[0] = True
        print(f'client: server replied at {get_time()}: {bytes_read.decode()}')
        print(f'client: you entered: {(user := input())}')
        print(f'client: sent to server at {get_time()}')
        s.send(user.encode())
    s.close()

def timer(exit_thread):
    i = 1
    while True:
        time.sleep(1)
        if exit_thread[0]:
            break
        print(f'client: at {get_time()} waiting for a response, {i} second{" has" if i < 1 else "s have"} elapsed')
        i += 1
    _thread.exit()

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == '__main__':
    main()
