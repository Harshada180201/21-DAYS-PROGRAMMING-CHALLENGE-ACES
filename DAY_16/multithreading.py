from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start() #internally it will call run() method
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Byeee")

'''
OUTPUT: Hello
        Hi
        Hello
        Hi
        Hello
        Hi
        Hello
        Hi
        Hello
        Hi
        Byeee
'''