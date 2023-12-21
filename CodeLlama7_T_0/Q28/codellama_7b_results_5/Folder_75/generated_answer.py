
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 62 and 83, both inclusive
    indices = [i for i, x in enumerate(char_list) if 62 <= ord(x) <= 83]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Get the 9th smallest ASCII value among the characters between indices 62 and 83, both inclusive
    nth_smallest = sorted_chars[indices[0]]
    return nth_smallest
