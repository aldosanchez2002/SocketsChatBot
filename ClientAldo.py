# Aldo Sanchez
import time
import threading
import datetime;

def get_time():
    x= datetime.datetime.now()
    return f"{x.hour}:{x.minute}:{x.second}"

def count(master):
    seconds=0
    while master.is_alive():
        if seconds!=0:
            print("client: at",get_time(), "waiting for response ",end="")
            if seconds==1:
                print("1 second has elapsed")
            else:
                print(seconds,"seconds have elapsed")
        seconds+=1
        time.sleep(1)
 
def receive(socket):
    global message
    message = socket.recv(10000).decode()
    print("client: server localhost replied at:",get_time())



def threads_recv(socket):
    reciever = threading.Thread(target=receive, args=(socket,))
    reciever.start()
    counter = threading.Thread(target=count, args=(reciever,))
    counter.start()
    reciever.join()
    return message

def getInput(file=0):
    if file:
        answer = file.readline()
        if not answer:
            return ""
        if answer[-1]=="\n":
            answer=answer[:-1]
        return answer.replace(","," ")

if __name__ == '__main__':
    from socket import *
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost",7070))
    try:
        f=open("FAKEFILE.txt", "r")
        print("Reading from file :")
        fileIn=getInput(f)
        x=threads_recv(s)
        while x and fileIn:
            print("clinet:",x)
            s.send(fileIn.encode())
            x=threads_recv(s)
            fileIn=getInput(f)
            if "EXIT" in x or not fileIn:
                exit()

    except FileNotFoundError:
        x=threads_recv(s)
        while x:
            print("clinet:",x)
            x=input()
            print("client: you entered: ",x)
            s.send(x.encode())
            print("client: sent to server at:",get_time())
            x=threads_recv(s)
            if "EXIT" in x:
                exit()
