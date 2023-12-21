
def filter_chars(s):
    # Create a new string with all characters removed
    new_string = ""

    # Iterate over each character in the given string
    for char in s:

        # Check if the current character is between indices 35 and 89, both inclusive
        if (char >= 'E' and char <= 't') and (35 <= char_index <= 89):

            # If so, skip this character when building the new string
            continue


        # Otherwise, add the current character to the new string
        new_string += char

    # Return the filtered string
    return new_string
