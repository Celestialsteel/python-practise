
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)
    #recursive function to calculate the factorial of a number

def main():
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is: {factorial(number)}")
    #takes input from the user and calls the function to calculate the factorial 

if __name__ == "__main__":
    main()
    #main function call