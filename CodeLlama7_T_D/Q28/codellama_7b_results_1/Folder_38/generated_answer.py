
def return_nth_smallest_ascii(string):
    # Get the indices of all characters in the string
    indices = []
    for char in string:
        indices.append(string.index(char))

    # Sort the indices by the ASCII value of the corresponding character
    sorted_indices = sorted(indices, key=lambda x: string[x])

    # Return the 10th smallest ASCII value
    return string[sorted_indices[9]]
