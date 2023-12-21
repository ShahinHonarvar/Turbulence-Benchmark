
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 51 and 78, both inclusive
    idx_list = [i for i, c in enumerate(char_list) if 51 <= i <= 78]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Get the character with the 9th smallest ASCII value
    nth_smallest = sorted_chars[idx_list[8]]
    return nth_smallest
