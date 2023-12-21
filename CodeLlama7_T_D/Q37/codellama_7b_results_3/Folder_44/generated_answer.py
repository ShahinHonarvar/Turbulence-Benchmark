
def filter_chars(s):
    # Create a list of characters in the string
    char_list = list(s)
    # Iterate over each character in the list
    for i, c in enumerate(char_list):
        # Check if the character is between indices 21 and 43, inclusive
        if 20 < i < 44:
            # Check if the character is greater than or equal to '+' and smaller than or equal to '8'
            if c >= "+" and c <= "8":
                # Remove all occurrences of the character from the list
                char_list.remove(c)
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
