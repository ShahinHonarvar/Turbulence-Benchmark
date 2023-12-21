
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between 3 and 26, both inclusive
    indices = []
    for i in range(len(string)):
        if 3 <= string[i] <= 'Z' or 3 <= string[i] <= 'z':
            indices.append(i)
    # Sort the characters by their ASCII values

    sorted_characters = sorted(string[indices[0]:indices[-1]+1]], key=lambda x: ord(x))
    # Return the character with the 5th smallest ASCII value among those characters

    return sorted_characters[4]
