
def filter_chars(my_string):
    # Initialize an empty string
    filtered_string = ""

    # Iterate over the characters of the input string
    for char in my_string:
        # If the character is between indices 43 and 80, both inclusive, and is greater than or equal to '=' and smaller than or equal to 'E', then remove it from the filtered string
        if (43 <= ord(char) <= 80) and ('=' <= char <= 'E'):
            continue

        # Otherwise, append the character to the filtered string

        else:
            filtered_string += char

    # Return the filtered string
    return filtered_string
