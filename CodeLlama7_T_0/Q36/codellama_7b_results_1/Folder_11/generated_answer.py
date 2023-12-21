
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between 86 and 93 (exclusive)
        if 86 < ord(char_list[i]) < 93:
            # If it is, remove all occurrences of that character in the string
            char_list = [c for c in char_list if c != char_list[i]]

    # Join the list of characters back into a string and return it
    return "".join(char_list)
