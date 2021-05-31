class Parent:
    def __init__(self):
        print("In Parent Class")

    def introParent(self):
        print("Welcome to Parent method")

class Child(Parent):
    def __init__(self):
        print("In Child Class")

    def introChild(self):
        print("Welcome to Parent method")

class ChildSon(Child):
    def __init__(self):
        print("In Child's son Class")

obj = ChildSon()
obj.introChild()
obj.introParent()