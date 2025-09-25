from os import name, system
from shapes import get_shape
#function to clear the screen of the output
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
         _ = system('clear')


#function to print the corresponding shape on the screen
def print_shapes(x):
    if x == 100:
        print(get_shape(0))

    elif x == 90 or x == 80:
        print(get_shape(1))

    elif x == 70 or x == 60:
        print(get_shape(2))
    
    elif x == 50 or x == 40:
        print(get_shape(3))

    elif x == 30 or x == 20:
         print(get_shape(4))

    elif x == 10 :
         print(get_shape(5))


def show_result(result):
    if result == 'winner':
        print(get_shape(100))
    else:
        print(get_shape(-1))