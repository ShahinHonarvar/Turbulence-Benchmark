
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between 587 and 648 (exclusive)
        if 587 < ord(char_list[i]) < 648:
            # Remove all occurrences of this character from the list
            char_list = [c for c in char_list if c != char_list[i]]
    # Join the characters back into a string and return it
    return "".join(char_list)
