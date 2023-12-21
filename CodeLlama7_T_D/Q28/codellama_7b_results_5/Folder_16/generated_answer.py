
def return_nth_smallest_ascii(s):
    # Get the indices of the characters in the string that occur between indices 18 and 45
    start = s.find('{')
    end = s.rfind('}')
    # Get the list of characters between these indices
    char_list = [char for char in s[start:end]]
    # Sort the list of characters by their ASCII value
    sorted_list = sorted(char_list, key=lambda x: ord(x))
    # Return the character with the 7th smallest ASCII value
    return sorted_list[6]
