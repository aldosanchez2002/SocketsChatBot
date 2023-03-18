#!/usr/bin/env python3
from socket import *
import time, random
s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 7070))
s.listen(5)
print("ChatBot Server Started", end=" ")
#set wait limit here
wait_limit=6
if wait_limit<10:
    print('low-delay')
else:
    print('high-delay')
while True:
    c,a = s.accept()
    print("Received connection from" , a)
    responses={
            "female":"How excellent! Are you a CS major?",
            "male": "Me Too. Are you a CS major?",
            }
    passed=False       
    time.sleep(int(wait_limit*random.random()))
    c.send("Hello, are you male or female?".encode())
    while not passed:
        answer=c.recv(10000).decode()
        time.sleep(int(wait_limit*random.random()))
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
        time.sleep(int(wait_limit*random.random()))
        if answer in responses:
            c.send(responses[answer].encode())
            passed = True
        else:
            c.send("Sorry, try again".encode())
    # Question 3
    answer=c.recv(10000).decode().split()
    time.sleep(int(wait_limit*random.random()))
    c.send(f'{answer[0]} are awesome, but I hate {answer[-1]} too, Bye for now.'.encode())
    c.close()
    # Server changes:
    # close the socket from the server side instead of sending an exit message
    # connect to correct port
