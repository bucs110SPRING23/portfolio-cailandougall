def multiplication(param1, param2):
    """
    This function multiplies two numbers using a loop and an accumulator
    args: param1(int), param2(int)
    return: result (int)
    """
    result=0
    for num in range (0, param2):
        result+=param1
    return result

def exponentiation(param1, param2):
    """
    This function raises a number to an exponent using multiplication
    args: param1(int), param2(int)
    return: result (int)
    """
    result=1
    for num in range (0, param2):
        result*=param1
    return result

def square(param1):
    """
    This function squares a number using the exponentiation function from above
    args: param1 (int), 2(int)
    return: exponentiation (param1, 2) (int)
    """
    return exponentiation (param1, 2)

def main():
    param1=int(input("enter param1: "))
    param2=int(input("enter param2: "))
    print (multiplication(param1, param2))
    param1=int(input("enter number: "))
    param2=int(input("enter exponent: "))
    print (exponentiation(param1, param2))
    param1=int(input("enter the parameter: "))
    print (square(param1))
main()
     

