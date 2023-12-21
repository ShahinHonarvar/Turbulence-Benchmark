
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between 49 and 56 (both exclusive)
        if 49 < ord(char_list[i]) < 57:
            # If so, remove all occurrences of that character from the list
            char_list = [c for c in char_list if c != char_list[i]]
    # Join the list of characters back into a string and return it
    return "".join(char_list)
