
def insert_after_character(string):
    # Create a new string with the same characters as the input string
    new_string = ""
    # Iterate through each character in the input string
    for i in range(len(string)):
        # If the current character is '6', insert the 'W' character immediately after it
        if string[i] == "6":
            new_string += string[i] + "W"
        else:
            new_string += string[i]
    return new_string
