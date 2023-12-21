
def insert_before_character(string, character):
    # Create a new string with the inserted character
    new_string = ""

    for i in range(len(string)):
        # If the current character is the specified character, insert the new character
        if string[i] == character:
            new_string += "X" + string[i]

        # Otherwise, just add the current character to the new string
        else:
            new_string += string[i]

    return new_string
