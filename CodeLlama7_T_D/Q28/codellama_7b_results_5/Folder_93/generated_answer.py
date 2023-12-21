
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters in the list that occur between 42 and 59
    indices = [i for i, x in enumerate(char_list) if 42 <= i <= 59]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list[min(indices):max(indices)+1], key=ord)
    # Return the 17th smallest ASCII value among those characters
    return sorted_chars[16]
