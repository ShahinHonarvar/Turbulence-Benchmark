
def return_nth_smallest_ascii(string):
    # Create a list of unique characters in the string
    char_list = list(set(string))
    # Sort the list of characters by their ASCII value
    sorted_list = sorted(char_list, key=lambda x: ord(x))
    # Return the 15th smallest ASCII value from the sorted list
    return sorted_list[14]
