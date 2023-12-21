
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over each character in the given string
    for c in s:

        # Check if the current character is between indices 513 and 877, both inclusive
        if 513 <= s.find(c) <= 877:

            # Check if the current character is greater than or equal to '?' and smaller than or equal to 'n'
            if c >= "?" and c <= "n":

                # Skip adding this character to the new string
                continue


        # Add the current character to the new string
        new_str += c

    # Return the filtered string
    return new_str
