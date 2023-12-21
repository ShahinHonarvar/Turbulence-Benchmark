
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""

    # Iterate over each character in the input string
    for char in s:

        # Check if the current character is between indices 19 and 33, both inclusive
        if (char >= 'S') and (char <= '{'):

            # Skip this character since it falls within the filtered range
            continue


        # Append the character to the new string
        new_string += char

    # Return the altered string
    return new_string
