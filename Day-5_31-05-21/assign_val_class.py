class Demo:
    name = ""

    #assign val by constructor
    def __init__(self, name):
        self.name = name

    #get val by method
    def func(self):
        print("My name is "+self.name)


ob = Demo("Harshil")
ob.func()



