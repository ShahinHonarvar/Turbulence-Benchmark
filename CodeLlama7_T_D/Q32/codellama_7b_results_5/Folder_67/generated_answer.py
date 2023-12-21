
def insert_after_character(string):
    # Create a new string with the same characters as the input string
    new_string = ""

    # Iterate over the characters in the input string
    for char in string:
        # If the current character is 'j', insert the character '1' immediately after it
        if char == 'j':
            new_string += "1" + char
        else:
            new_string += char

    return new_string
