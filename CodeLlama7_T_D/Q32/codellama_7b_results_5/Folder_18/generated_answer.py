
def insert_after_character(string, character):
    # Create a new string with the same characters as the input string
    new_string = ""
    for i in range(len(string)):
        # If the current character is equal to the target character, append the target character followed by the inserted character
        if string[i] == character:
            new_string += string[i] + "l"
        else:
            # Otherwise, just append the current character to the new string
            new_string += string[i]
    return new_string
