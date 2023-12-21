
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string that occur between indices 12 to 72, both inclusive
    indices = []
    for i in range(len(string)):
        if i >= 12 and i <= 72:
            indices.append(i)
    # Sort the indices based on the ASCII values of the corresponding characters in the string
    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))
    # Return the character with the 13th smallest ASCII value among those characters in the string that occur between indices 12 to 72, both inclusive.
    return string[sorted_indices[12]]
