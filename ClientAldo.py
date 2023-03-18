import time, threading, datetime;
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
    try:
         message = socket.recv(10000).decode()
         print("client: server localhost replied at:",get_time())
    except Exception:
         print("Connection terminated by Server at:",get_time())
         message="Server Closed Connection"
def threads_manager(socket):
    reciever = threading.Thread(target=receive, args=(socket,))
    reciever.start()
    counter = threading.Thread(target=count, args=(reciever,))
    counter.start()
    reciever.join()
    if message=="Server Closed Connection":
        exit()
    return message
def getFileInput(file=0):
    if file:
        answer = file.readline()
        if not answer:
            return ""
        if answer[-1]=="\n":
            answer=answer[:-1]
        return answer.replace(","," ")
def fileChatBot(file):
    print("Reading from file :")
    fileIn=getFileInput(f)
    x=threads_manager(s)
    while x and fileIn:
        print("client:",x)
        s.send(fileIn.encode())
        x=threads_manager(s)
        fileIn=getFileInput(f)
        if not fileIn:
            exit()
def terminalChatBot(s):
    x=threads_manager(s)
    while x:
        print("client:",x)
        x=input()
        print("client: you entered: ",x)
        s.send(x.encode())
        print("client: sent to server at:",get_time())
        x=threads_manager(s)
if __name__ == '__main__':
    from socket import *
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost",7069))
    try:
        f=open("FAKEFILE.txt", "r")
        fileChatBot(f)
    except FileNotFoundError:
        terminalChatBot(s)
# Client changes:
# conect to correct port
# add try block before reading to prevent a broken pipe error when the socket is closed
# removed the check for a termination message in the recv content
# broke down methods to improve readability
