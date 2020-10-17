'''1.Duck Typing'''

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

ide = PyCharm()
lap1 = Laptop()
lap1.code(ide)

ide = MyEditor()
lap2 = Laptop()
lap2.code(ide)

'''
OUTPUT: Compiling
        Running
        Spell Check
        Convention Check
        Compiling
        Running
'''