
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)

    # Get the indices of all the characters between 33 and 60, inclusive
    indices = [i for i, c in enumerate(char_list) if 33 <= ord(c) <= 60]

    # Sort the indices by the corresponding character's ASCII value
    sorted_indices = sorted(indices, key=lambda x: char_list[x])

    # Return the character with the 18th smallest ASCII value among those characters in the string that occur between indices 33 to 60, both inclusive.
    return char_list[sorted_indices[17]]
