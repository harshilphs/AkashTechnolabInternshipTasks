class Parent1:
    def __init__(self):
        print("In Parent1 Class")

    def introParent1(self):
        print("Welcome to Parent1 method")

class Parent2:
    def __init__(self):
        print("In Parent2 Class")

    def introParent2(self):
        print("Welcome to Parent2 method")

class Child(Parent1,Parent2):
    def __init__(self):
        print("In Child's son Class")

ob = Child()
ob.introParent1()
ob.introParent2()