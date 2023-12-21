
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = []
    for char in string:
        if char not in char_list:
            char_list.append(char)
    # Sort the character list by ASCII value
    char_list.sort(key=ord)
    # Return the 8th smallest ASCII value
    return char_list[7]
