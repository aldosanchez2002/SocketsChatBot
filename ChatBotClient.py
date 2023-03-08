# Aldo Sanchez
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
        f=open("FAKE.txt", "r")
        print("Reading from file :")
        fileIn=getInput(f)
        x=s.recv(10000).decode()
        while x and fileIn:
            print(x)
            s.send(fileIn.encode())
            x=s.recv(10000).decode()
            fileIn=getInput(f)
            if "EXIT" in x or not fileIn:
                exit()

    except FileNotFoundError:
        x=s.recv(10000).decode()
        while x:
            print(x)
            s.send(input().encode())
            x=s.recv(10000).decode()
            if "EXIT" in x:
                exit()