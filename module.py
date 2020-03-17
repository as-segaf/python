# Simply, a module is a file consisting of Python code.
# A module can define functions, classes and variables.
# A module can also include runnable code.
def say_hello(name):
    print("Hello:",name)
    return

def print_str(str):
    print("your name is:",str)
    return

def print_filename():
    print("module file name is:",__name__)
    return