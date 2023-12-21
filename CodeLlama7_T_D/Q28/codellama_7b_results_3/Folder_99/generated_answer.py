
def return_nth_smallest_ascii(string):
    # Get the indices of all characters in the string that occur between indices 17 and 65, both inclusive
    indices = []
    for i in range(len(string)):
        if (i >= 17 and i <= 65) and (string[i] not in indices):
            indices.append(i)

    # Sort the indices in ascending order based on the ASCII value of the corresponding character

    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))

    # Return the 8th smallest ASCII value among those characters in the string that occur between indices 17 to 65, both inclusive.

    return string[sorted_indices[7]]
