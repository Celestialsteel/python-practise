# How to approach this problem:
# 1. Get the number from the user
# 2. Find a way to isolate the digits in the number(possibly convert to string)
# 3. Loop through the digits and add them to a list
# 4. Calculate the sum of the digits in the list


"""
def isolate_digits():
    digits = []
    for i in range(10):  # Loop through numbers 0 to 9
        digits += [i]    # Add each number to the list
    return digits
    #needed a function to isolate the digits in the number to check if the number is a digit or not. 
    #Turned out to be unnecessary since the input is already a number
"""
def sum_Of_num(a):
    sum = 0
    for i in str(a):
        sum=sum+int(i)
    return sum

def main():
    num = int(input("Enter a number: "))  #requests for user input in form of a number
    #digits = isolate_digits()#passes the number to isolate digits function to check if the number is a digit
    print(f"The digits in the number are: ", [int(i) for i in str(num)])
    print("The sum of the digits in the number is:", sum_Of_num(num))
    #prints out the sum of the digits in the number by calling the sum_Of_num function


if __name__ == "__main__":
    main()
    #main function call execs the prograam

