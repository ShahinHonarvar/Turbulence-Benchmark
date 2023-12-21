
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over the characters in the given string
    for c in s:
        # Check if the character is between indices 515 and 538, both inclusive
        if (515 <= s.index(c)) and (s.index(c) <= 538)):
            # Check if the character is greater than or equal to '+' and smaller than or equal to '}'
            if c >= "+" and c <= "}":
                # Remove all occurrences of the character from the new string
                new_str = new_str.replace(c, "")
            else:
                # Add the character to the new string
                new_str += c
    return new_str
