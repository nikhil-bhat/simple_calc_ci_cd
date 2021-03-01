def add(number1,number2):
    return number1+number2

def subtract(number1,number2):
    return number1-number2    

def multiply(number1,number2):
    return number1*number2   

def divide(number1,number2):
    return number1/number2     


if __name__ == "__main__":
    number1 = int(input("Enter a number: \n"))
    number2 = int(input("Enter a number: \n"))
    add_result = add(number1,number2)
    sub_result = subtract(number1,number2)
    mult_result = multiply(number1,number2)
    divide_result = divide(number1,number2)

    report = (
        f"The numbers were {number1} and {number2}"
        f"The result of addition was {add(number1,number2)}"
        f"The result of subtraction was {subtract(number1,number2)}"
        f"The result of multiplication was {multiply(number1,number2)}"
        f"The result of division was  {divide(number1,number2)}"
    )
    print(report)

