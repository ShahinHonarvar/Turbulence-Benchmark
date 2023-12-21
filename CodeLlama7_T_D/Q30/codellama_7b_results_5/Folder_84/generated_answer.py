
def insert_before_character(string, character):
    # Create a new string with the desired characters
    new_string = ""

    # Iterate through each character in the original string
    for char in string:
        # If the current character is the one we want to insert before
        if char == character:
            # Insert the desired character immediately before it
            new_string += "n" + char
        else:
            # Otherwise, just append the current character to the new string
            new_string += char

    # Return the new string with the inserted character
    return new_string
