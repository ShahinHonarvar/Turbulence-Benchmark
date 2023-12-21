
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between indices 24 and 71, both inclusive
    indices = [i for i, c in enumerate(string) if 24 <= i <= 71]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(indices, key=lambda x: ord(string[x]))
    # Return the character with the 8th smallest ASCII value among those characters
    return string[sorted_chars[7]]
