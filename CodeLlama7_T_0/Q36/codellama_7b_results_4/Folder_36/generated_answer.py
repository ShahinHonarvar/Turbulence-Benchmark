
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between 283 and 484 (exclusive)
        if 283 < ord(char_list[i]) < 484:
            # If it is, remove all occurrences of that character in the string
            char_list = [c for c in char_list if c != char_list[i]]
    # Return the altered string
    return "".join(char_list)
