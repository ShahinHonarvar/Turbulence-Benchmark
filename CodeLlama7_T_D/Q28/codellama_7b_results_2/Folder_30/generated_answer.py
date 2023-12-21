
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters that occur between indices 50 and 76
    indices = [i for i, x in enumerate(char_list) if 50 <= i <= 76]
    # Sort the indices based on the ASCII values of the corresponding characters
    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))
    # Return the character with the 11th smallest ASCII value among those characters in the string that occur between indices 50 to 76, both inclusive.
    return string[sorted_indices[10]]
