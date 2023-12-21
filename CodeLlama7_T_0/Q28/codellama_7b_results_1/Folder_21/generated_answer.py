
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 8 and 65 (inclusive)
    indices = [i for i, x in enumerate(char_list) if 8 <= ord(x) <= 65]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Get the 6th smallest ASCII value among the characters between indices 8 and 65 (inclusive)
    6th_smallest = sorted_chars[indices[0]]
    return 6th_smallest
