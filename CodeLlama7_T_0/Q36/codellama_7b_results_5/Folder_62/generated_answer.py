
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the original string
    for char in string:
        # If the current character is between 63 and 89 (both exclusive) and is greater than '*' and smaller than 'w', remove all occurrences of that character from the filtered string
        if 63 < ord(char) < 89 and ord(char) > ord('*') and ord(char) < ord('w'):
            filtered_string = filtered_string.replace(char, "")

        # Otherwise, add the current character to the filtered string
        else:
            filtered_string += char

    # Return the filtered string
    return filtered_string
