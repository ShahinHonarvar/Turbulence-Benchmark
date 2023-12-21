
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string
    indices = []
    for char in string:
        indices.append(string.index(char))

    # Sort the indices by the ASCII value of the corresponding character
    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))

    # Return the 11th smallest ASCII value
    return ord(string[sorted_indices[10]])
