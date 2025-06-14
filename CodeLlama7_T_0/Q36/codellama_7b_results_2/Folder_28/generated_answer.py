
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over each character in the input string
    for char in s:

        # If the current character is between 31 and 73 (exclusive)
        if 31 < ord(char) < 73:

            # And it is greater than 'M' and smaller than 'j'
            if char > 'M' and char < 'j':

                # Skip this character in the new string
                continue


        # Add the current character to the new string
        new_str += char

    # Return the filtered string
    return new_str
