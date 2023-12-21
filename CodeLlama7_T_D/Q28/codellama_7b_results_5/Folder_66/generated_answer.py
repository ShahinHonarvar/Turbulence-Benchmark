
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters in the list that occur between indices 35 and 52 (both inclusive)
    indices = [i for i, c in enumerate(char_list) if 35 <= i <= 52]
    # Sort the indices by the corresponding ASCII values
    sorted_indices = sorted(indices, key=lambda x: ord(char_list[x]))
    # Return the character with the 10th smallest ASCII value among those characters in the string that occur between indices 35 and 52 (both inclusive)
    return char_list[sorted_indices[9]]
