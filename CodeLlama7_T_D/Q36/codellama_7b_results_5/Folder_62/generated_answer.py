
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Iterate over each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between 63 and 89 (both exclusive)
        if 63 < ord(char_list[i]) < 89:
            # If it is, remove all occurrences of that character in the string
            char_list = [x for x in char_list if x != char_list[i]]
    # Return the altered string
    return "".join(char_list)
