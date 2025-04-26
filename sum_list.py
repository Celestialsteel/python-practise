
numlist=[]
#starting with an empty list to store the numbers with no fixed size since it's supposed to be a list
def sum_list(numlist):
    total = 0
    for num in numlist:
        total += num
    return total

#function to calculate the sum of the list
def main():
    count=int(input("Enter the number of elements in the list you wish to add:"))
    #taking the number of elements in the list as input from the user
    numlist=[0]*count #had to consult this from AI since traceback error came up without it
    for i in range(count):
        numlist[i]=int(input(f"Enter element {i+1}: "))
    print("The sum of the list is:", sum_list(numlist))

if __name__ == "__main__":
        main()