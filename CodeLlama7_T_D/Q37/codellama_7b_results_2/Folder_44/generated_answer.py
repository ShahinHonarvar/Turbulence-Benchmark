
def filter_chars(s):
    # Create a new string that will contain the filtered characters
    new_str = ""

    # Iterate over the characters in the original string
    for char in s:

        # If the character is between indices 21 and 43, both inclusive, and is greater than or equal to character '+' and smaller than or equal to character '8', then remove all occurrences of that character from the new string
        if (21 <= char_index <= 43) and (char >= '+' and char <= '8'):
            continue

        # Otherwise, add the character to the new string
        else:
            new_str += char

    # Return the altered string
    return new_str
