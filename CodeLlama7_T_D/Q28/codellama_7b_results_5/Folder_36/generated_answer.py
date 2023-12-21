
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between indices 17 and 56, both inclusive.
    indices = []
    for i in range(17, len(string)):
        if string[i] in string[17:56]:
            indices.append(i)
    # Sort the indices by the ASCII values of the corresponding characters.
    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))
    # Return the character with the 9th smallest ASCII value among those characters in the string that occur between indices 17 to 56, both inclusive.
    return string[sorted_indices[8]]
