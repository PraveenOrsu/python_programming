user_input=input("Enter a character")

def input_check(char):
    if char.isdigit():
        return "you enter a digit "
    elif char.islower():
        return "you enter a lower case letter"
    elif char.isupper():
        return "you enter a upper case letter"
    else:
        return "you enter input is neither  a digit nor a letter"
    
print(f"{input_check(user_input)} is {user_input}")j
