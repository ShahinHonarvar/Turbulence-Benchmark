
def insert_before_character(string):
    # Create a new string with the same characters as the input string
    new_string = ""
    # Iterate through each character in the input string
    for char in string:
        # If the current character is 'P', insert the character 'V' before it
        if char == "P":
            new_string += "V" + char
        else:
            new_string += char

    return new_string
