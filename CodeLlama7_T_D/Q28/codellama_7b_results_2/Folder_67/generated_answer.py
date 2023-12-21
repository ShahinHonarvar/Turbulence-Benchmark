
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Get the indices of the characters that occur between 60 and 83
    indices = [i for i, x in enumerate(char_list) if 60 <= ord(x) <= 83]
    # Sort the indices based on the ASCII values of the corresponding characters
    sorted_indices = sorted(indices, key=lambda x: ord(char_list[x]))
    # Return the character with the 14th smallest ASCII value among those that occur between indices 60 to 83, both inclusive
    return char_list[sorted_indices[14]]
