
def insert_before_character(string, char):
    # Create a new empty string to store the result
    result = ""

    # Loop through each character in the input string
    for c in string:
        # If the current character is the specified character, insert the other character before it
        if c == char:
            result += "H" + c
        # Otherwise, just append the current character to the result string
        else:
            result += c

    # Return the new string with the specified character inserted
    return result
