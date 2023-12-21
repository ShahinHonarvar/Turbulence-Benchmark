
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the original string
    for char in string:

        # If the current character is between 52 and 88,
        if 52 < ord(char) < 88:

            # Check if the current character is greater than '&' and smaller than 'c'
            if ord(char) > ord('&') and ord(char) < ord('c'):

                # If the condition is true, continue to the next character in the original string
                continue


        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
