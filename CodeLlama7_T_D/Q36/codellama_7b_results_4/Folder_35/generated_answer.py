
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate through each character in the given string
    for char in s:

        # If the current character is between indices 163 and 658 (exclusive)
        if 163 < ord(char) < 658:

            # And it is greater than '(' and smaller than ']'
            if char > "(" and char < "]":

                # Skip this character in the new string
                continue

        # Add the current character to the new string
        new_str += char

    # Return the filtered string
    return new_str
