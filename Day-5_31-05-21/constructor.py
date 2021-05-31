# it A constructor is a class function that instantiates an object to predefined values.


class MyClass:
    # default constructor

    # def __init__(self):
    #     print("Hello World!")

    # parameterized constructor

    def __init__(self, name):
        print("Hello World")
        print(name)

ob = MyClass("Harshil")