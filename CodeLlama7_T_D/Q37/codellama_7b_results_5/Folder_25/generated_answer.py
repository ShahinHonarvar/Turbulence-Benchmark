
def filter_chars(my_string):
    # Create a new string without the filtered characters
    new_string = ""

    # Iterate over each character in the input string
    for char in my_string:

        # If the current character is between indices 31 and 38, both inclusive, and is greater than or equal to character ';' and smaller than or equal to character 'g', then remove it from the new string
        if (char >= ';') and (char <= 'g'):
            continue

        # Otherwise, add the current character to the new string
        else:
            new_string += char

    # Return the altered string
    return new_string
