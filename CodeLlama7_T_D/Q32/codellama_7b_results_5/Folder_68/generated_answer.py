
def insert_after_character(string, character):
    # Create a new string with the same contents as the original string
    new_string = ""
    # Loop through each character in the original string
    for char in string:
        # If the current character is the one to insert after, append the new character and then append the rest of the original string
        if char == character:
            new_string += "0" + char
        # Otherwise, just append the current character to the new string
        else:
            new_string += char
    # Return the new string with the inserted character
    return new_string
