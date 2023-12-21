
def filter_chars(s):
    # Create a list of characters in the string
    char_list = list(s)
    # Initialize a variable to keep track of the number of characters removed
    num_removed = 0
    # Iterate over the characters in the string
    for i, c in enumerate(char_list):
        # If the current character is between indices 86 and 92, both inclusive, and is greater than or equal to character '!' and smaller than or equal to character 's', remove all occurrences of that character from the string
        if i >= 86 and i <= 92 and c >= "!" and c <= "s":
            # Remove the current character from the string
            char_list.remove(c)
            # Increment the number of characters removed
            num_removed += 1
    # Return the altered string
    return "".join(char_list)
