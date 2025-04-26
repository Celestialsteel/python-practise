def loop_factorial(a):
    if a == 0:  # Base case where the factorial of 0 is 1
        return 1
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
    return factorial
  #Using a for loop to calculate the factorial of a number

def main():
    number=int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is: {loop_factorial(number)}")
    #takes input from the user and calls the function to calculate the factorial  


if __name__=="__main__":
    main()
    #main function call