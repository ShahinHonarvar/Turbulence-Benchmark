
def filter_chars(string):
    # Create a new string with all characters removed
    filtered_string = ""

    # Iterate through each character in the given string
    for char in string:
        # Check if the current character is between indices 11 and 72, both inclusive
        if (char.isalpha() and 11 <= ord(char) <= 72):
            # Check if the current character is greater than or equal to 'i' and smaller than or equal to 'v'
            if ('i' <= char <= 'v'):
                # Remove all occurrences of the current character from the filtered string
                filtered_string = filtered_string.replace(char, "")
        else:
            # Add the current character to the filtered string
            filtered_string += char

    return filtered_string
