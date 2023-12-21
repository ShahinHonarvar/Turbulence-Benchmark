
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 17 to 56 from the string
    sub_str = string[17:56+1]
    # Create a list of all the unique characters in the sub-string
    char_list = list(set(sub_str))
    # Sort the list of characters by their ASCII value
    char_list.sort(key=ord)
    # Return the character with the 9th smallest ASCII value
    return char_list[8]
