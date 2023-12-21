
def return_nth_smallest_ascii(s):
    # Convert the string to a list of characters
    char_list = list(s)
    # Get the indices of the characters that occur between indices 17 and 86, both inclusive
    indices = [i for i in range(17, 86 + 1) if char_list[i] in char_list[:86]]
    # Sort the characters by their ASCII value
    sorted_chars = sorted(char_list[indices[0]:indices[-1] + 1]], key=lambda x: ord(x))
    # Return the 15th smallest ASCII value among the characters in the specified range
    return sorted_chars[14]
