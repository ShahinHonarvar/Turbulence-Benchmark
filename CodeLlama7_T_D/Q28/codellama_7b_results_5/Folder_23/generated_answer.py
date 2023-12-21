
def return_nth_smallest_ascii(s):
    # Find the indices of the characters in the string that occur between 29 and 47
    start_idx = s.find('a', 29)
    end_idx = s.rfind('z', 47)
    # Create a list of all the characters in the string between the indices found above
    char_list = s[start_idx:end_idx+1]
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 7th smallest ASCII value in the sorted list
    return sorted_list[6]
