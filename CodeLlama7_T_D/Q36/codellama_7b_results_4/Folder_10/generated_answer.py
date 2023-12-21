
def filter_chars(s):
    # Create a new string with the same length as the original string
    new_string = ""

    # Iterate over the characters in the original string
    for char in s:

        # If the current character is between 35 and 60 (both exclusive) and it is greater than '!' and smaller than 'B', then remove all occurrences of that character from the new string while keeping the order of all characters intact.
        if 35 < char < 60 and char > "!" and char < "B":
            new_string = new_string.replace(char, "")

    # Return the altered string
    return new_string
