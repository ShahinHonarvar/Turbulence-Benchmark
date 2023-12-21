
def return_nth_smallest_ascii(string):
    # Get the characters between indices 5 and 10
    char_list = string[5:11]
    # Sort the characters in ascending order of their ASCII values
    sorted_char_list = sorted(char_list, key=ord)
    # Return the character with the 6th smallest ASCII value
    return sorted_char_list[5]
