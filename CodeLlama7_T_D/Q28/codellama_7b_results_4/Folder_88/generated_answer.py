
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between 38 and 64
    indices = [i for i, c in enumerate(string) if 38 <= i <= 64]
    # Sort the indices based on their corresponding ASCII values
    sorted_indices = sorted(indices, key=lambda x: ord(string[x]))
    # Return the character with the 14th smallest ASCII value among those characters in the string that occur between indices 38 to 64, both inclusive.
    return string[sorted_indices[13]]
