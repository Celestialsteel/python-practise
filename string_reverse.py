#string="This is my string message to be reversed"
string=""

#Starting with my own preconfigured message

def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

# Looping through characters as it makes the switch of ceharacters in empty reversed_string memory location

def main():
    string = input("Enter a string to reverse: ")
    reversed_string = reverse_string(string)
    print("Reversed string:", reversed_string)

  #main method to take user input and call the function to reverse the string
    
if __name__ == "__main__":
    main()
    #calls the main function to execute the program