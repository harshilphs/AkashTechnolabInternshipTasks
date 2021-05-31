class Parent:
    def __init__(self):
        print("In Parent Class")

    def introParent(self):
        print("Welcome to Parent method")

class Child1(Parent):
    def __init__(self):
        print("In Child1 Class")

    def introChild1(self):
        print("Welcome to Child1 method")

class Child2(Parent):
    def __init__(self):
        print("In Child2 Class")

    def introChild2(self):
        print("Welcome to Child2 method")

ob = Child1()
ob.introParent()
ob1 = Child2
ob.introParent()