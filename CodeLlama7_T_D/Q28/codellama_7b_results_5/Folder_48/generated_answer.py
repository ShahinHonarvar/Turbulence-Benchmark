
def return_nth_smallest_ascii(s):
    # Find the indices of the characters that occur between 37 and 59
    start_idx = s.find('a', 37)
    end_idx = s.rfind('z', 59)
    # Create a list of all the characters in the specified range
    char_list = []
    for i in range(start_idx, end_idx + 1):
        char_list.append(s[i])
    # Sort the list of characters by their ASCII values
    char_list.sort(key=ord)
    # Return the 6th smallest ASCII value among the characters in the specified range
    return char_list[5]
