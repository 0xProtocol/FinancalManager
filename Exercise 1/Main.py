

def Main(argument):
        if argument == "5":
            A5()
        elif argument == "6":
            A6()

def A5():
        print("Before Swap:")
        x = int(input('x: '))
        y = int(input('y: '))

        x = y*x;
        y = x/y;
        x = x /y;

        print("After Swap:")
        print ("x: " + str(x).replace('.0', ''))
        print("y: " + str(y).replace('.0', ''))

def A6():
    n1 = int(input('n1: '))
    n2 = int(input('n2: '))

    if n1 > n2:
     print("n1 > n2")
    elif n1 == n2:
     print("n1 and n2 are equal")
    elif n1 < n2:
     print("n1 < n2")


argument = input('Enter: ')
Main(argument)
