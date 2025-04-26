def checknumber(a):
    if a % 2 == 0:
        return print("The number is even")
    else:
        return print("The number is odd")
    #uses modulus operator to check if the number is odd or even

def main():
    num = int(input("Enter a number: "))
    checknumber(num)
    #takes input from the user and calls the function to check if the number is odd or even
if __name__ == "__main__":
    main()
    #calls the main function to execute the program