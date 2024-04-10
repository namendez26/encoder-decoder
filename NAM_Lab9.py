
def menu():
    global user_choice
    print("\nMenu\n-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n\n")
    user_choice = input("Please enter an option: ")

def encode(string):
    
    new_string = [] # Initializes list.
    
    for i in string: # Iterates through argument.
        i = int(i) # Temporarily conforms string to integer.
        i += 3 # Adds three, per encoder.
        if i > 9: # If i is greater than 9, ...
            i %= 10 # Then we'll need to lop off the first digit.
        new_string.append(str(i)) # Puts encoded digit into list

    return "".join(new_string) # Returns all list items joined together.

def main():

    # Initialize.
    menu_check = True

    while menu_check:
        menu() # Prints menu.
        if user_choice == '1':
            # 1. Encode
            og_pw = input("Please enter your password to encode: ")
            pw1 = encode(og_pw)
            print("Your password has been encoded and stored!")
        if user_choice == '2':
            # 2. Encode
            pass
        elif user_choice == '3':
            # 3. Quit
            menu_check = False

if __name__ == "__main__":
    main()