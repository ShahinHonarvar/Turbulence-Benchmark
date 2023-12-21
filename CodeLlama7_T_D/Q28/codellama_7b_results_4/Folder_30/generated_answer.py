
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string that occur between 50 and 76, both inclusive
    indices = []
    for i in range(len(string)):
        if 50 <= i <= 76:
            indices.append(i)
    # Sort the indices based on the ASCII value of the corresponding characters in the string
    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))
    # Return the character with the 11th smallest ASCII value among those characters
    return string[sorted_indices[10]]
