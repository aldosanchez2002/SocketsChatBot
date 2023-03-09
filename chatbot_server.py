#!/usr/bin/env python3
from socket import *
import time

def main():
    q1 = {
            'female' : 'How excellent! Are you a CS major?',
            'male' : 'Me too. Are you a CS major?',
            'default' : 'Alright. Are you a CS major?'
    }

    q2 = {
        'no' : 'Too bad. Anyway, what\'s an animal you like and two you don\'t',
        'yes' : 'Excellent, I am too. What\'s an animal you don\'t like and two you do?',
        'default' : 'Ok... What\'s an animal you don\'t like and two you do?'
    }

    q3 = {
        'default' : ''
    }

    clean_str = lambda s : ''.join(c.lower() for c in s if c.isalnum() or c in {' ', '\''})

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("localhost", 7069))
    s.listen(5)
    while True:
        c,a = s.accept()
        print("Received connection from" , a)
        c.send('Hello, are you male or female?'.encode())
        for q in (q1, q2, q3):
            res = c.recv(1024).decode().lower()
            print(res)
            c.send(q[res if res in q else 'default'].encode())
        animals = clean_str(res).split()
        c.send((('' if not animals else f'{animals[0]} awesome, but I hate {animals[-1]} too.') + ' Bye for now.').encode())
        c.close()

if __name__ == '__main__':
    main()