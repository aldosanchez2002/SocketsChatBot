#!/usr/bin/env python3
from socket import *
import time
s = socket(AF_INET, SOCK_STREAM)

# PART A
s.connect(("nigelward.com",80))
s.send("GET / HTTP/1.1\nHost: nigelward.com\n\n".encode())
s.recv(1000)
print(s.recv(11).decode())
s.recv(989)
print(s.recv(11).decode())
s.close()


# PART B
s = socket(AF_INET, SOCK_STREAM)
s.connect(("",7069))
    #B1
recievedB = int.from_bytes(s.recv(1024), byteorder="big")
print("big to big",recievedB)
    #B2
recievedL = int.from_bytes(s.recv(1024), byteorder="little")
print("big to little",recievedL)
    #B3
recieved = ntohs(int.from_bytes(s.recv(1024)))
print("big to your device",recieved)
if recieved == recievedL: 
    print("Your device is little endian")
else:
    print("Your device is big endian")
s.close()

#PART C Server

s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 7070))
s.listen(5)
print("ChatBot Server Started")
while True:
    c,a = s.accept()
    print("Received connection from" , a)
    responses={
            "female":"How excellent! Are you a CS major?",
            "male": "Me Too. Are you a CS major?",
            }
    passed=False
    while not passed:
        c.send("Hello, are you male or female?".encode())
        answer=c.recv(10000).decode()
        if answer in responses:
            c.send(responses[answer].encode())
            passed=True
        else:
            c.send(f"Sorry, I don't understand what {answer} means, try again".encode())

    # Question 2
    responses = {
        "no": "Too bad. Anyway, what's an animal you like and two you don't?",
        "yes": "Excellent, I am too. What's an animal you don't like and two you do?",
    }
    passed=False
    while not passed:
        answer=c.recv(10000).decode()
        if answer in responses:
            c.send(responses[answer].encode())
            passed = True
        else:
            c.send("Sorry, try again".encode())

    # Question 3
    answer=c.recv(10000).decode().split()
    c.send(f'{answer[0]} are awesome, but I hate {answer[-1]} too, Bye for now.'.encode())
    time.sleep(0.5)
    c.send("EXIT".encode())