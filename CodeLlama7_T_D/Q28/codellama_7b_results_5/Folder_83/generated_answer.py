
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string between indices 30 and 70
    char_list = [char for char in string if 30 <= string.index(char) <= 70]
    # Sort the list of characters by their ASCII value
    sorted_char_list = sorted(char_list, key=lambda x: ord(x))
    # Return the 15th smallest character in the sorted list
    return sorted_char_list[14]
