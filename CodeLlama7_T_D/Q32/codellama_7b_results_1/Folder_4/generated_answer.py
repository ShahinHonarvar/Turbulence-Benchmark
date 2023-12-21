
def insert_after_character(string):
    # Create a new string to store the modified characters
    new_string = ""
    # Loop through each character in the original string
    for i, char in enumerate(string):
        # If the current character is 'a', add the character '6' after it
        if char == "a":
            new_string += char + "6"
        # Otherwise, just add the current character to the new string
        else:
            new_string += char
    return new_string
