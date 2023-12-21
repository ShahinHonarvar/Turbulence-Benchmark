
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between 38 and 82, both inclusive
    indices = [i for i, char in enumerate(string) if 38 <= i <= 82]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(indices, key=lambda i: string[i])
    # Return the character with the 20th smallest ASCII value among those characters in the string that occur between indices 38 to 82, both inclusive.
    return sorted_chars[19]
