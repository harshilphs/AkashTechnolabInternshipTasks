class Parent:
    def __init__(self):
        print("In Parent Class")

    def intro(self):
        print("Welcome to Parent method")

class Child(Parent):
    def __init__(self):
        print("In Child Class")

obj = Child()
obj.intro()