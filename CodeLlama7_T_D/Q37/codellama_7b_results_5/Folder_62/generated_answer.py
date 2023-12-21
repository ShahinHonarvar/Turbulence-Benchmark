
def filter_chars(my_string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate through each character in the original string
    for char in my_string:

        # If the current character is between indices 10 and 69, inclusive
        if 10 <= my_string.index(char) <= 69:

            # And it is greater than or equal to 'I' and smaller than or equal to 'K'
            if char >= "I" and char <= "K":

                # Then skip adding it to the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
