
def return_nth_smallest_ascii(s):
    # Find the indices of the characters in the string
    start = s.index("25")
    end = s.index("77") + 1
    # Create a list of all the characters between the indices
    char_list = [c for c in s[start:end]]
    # Sort the list of characters by their ASCII values
    sorted_char_list = sorted(char_list, key=ord)
    # Return the 16th smallest ASCII value from the sorted list
    return sorted_char_list[15]
