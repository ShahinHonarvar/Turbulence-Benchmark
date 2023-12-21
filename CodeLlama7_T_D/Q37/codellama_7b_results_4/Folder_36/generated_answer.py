
def filter_chars(s):
    # Create a list of characters in the given string
    char_list = list(s)
    # Initialize a new string variable to store the filtered characters
    filtered_string = ""

    # Iterate through each character in the list
    for char in char_list:
        # Check if the current character falls between indices 259 and 502, both inclusive
        if (char_list.index(char) >= 259) and (char_list.index(char) <= 502):
            # Check if the current character is greater than or equal to ',' and smaller than or equal to '3'
            if (ord(char) >= ord(',') and ord(char) <= ord('3')):
                # Do not include this character in the filtered string
                continue

        # Add this character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
