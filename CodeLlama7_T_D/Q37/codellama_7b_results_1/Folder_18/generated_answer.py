
def filter_chars(my_string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate through each character in the input string
    for char in my_string:

        # Check if the current character is between indices 770 and 970, inclusive
        # and is greater than or equal to '-' and smaller than or equal to 'D'
        if (770 <= my_string.index(char) <= 970) and ('-' <= char <= 'D'):

            # If the current character meets the criteria, do not add it to the filtered string
            continue

        else:

            # Otherwise, add the current character to the filtered string
            filtered_string += char

    # Return the filtered string
    return filtered_string
