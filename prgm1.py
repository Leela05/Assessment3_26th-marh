def armstrong(number):
    sum = 0
    temp = number
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    if number == sum:
       return "Armstrong number"
    else:
       return "Not an Armstrong number"

def divisible_by_5(number):
    if number % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible by 5"

def Largest(num1, num2, num3):
    if num1 > num2 and num1 > num2:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == "__main__":
    # armstrong or not
    print("To check the number is armstrong or not")
    number = int(input("Enter the Number : "))
    result = armstrong(number)
    print(result)

    # divisible by 5 or not
    print("To check divisible by 5 or not")
    number = int(input("Enter the Number : "))
    result=divisible_by_5(number)
    print(result)

    # largest among 3 numbers
    print("to check greatest of 3 numbers")
    num1 = int(input("Enter num 1 : "))
    num2 = int(input("Enter num 2 : "))
    num3 = int(input("Enter num 3 : "))
    result = Largest(num1, num2, num3)
    print(result)

    # even or odd num
    print("to check odd or even")
    number = int(input("Enter the Number : "))
    result = even_or_odd(number)
    print(result)
