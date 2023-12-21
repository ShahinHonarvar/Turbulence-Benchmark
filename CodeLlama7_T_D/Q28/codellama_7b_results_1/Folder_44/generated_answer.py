
def return_nth_smallest_ascii(s):
    # Find the indices of the characters in the string
    indices = []
    for i, c in enumerate(s):
        if c not in indices:
            indices.append(i)
    # Get the character with the 8th smallest ASCII value
    char_with_smallest_ascii = None
    for i in range(20, 31):
        if s[i] < char_with_smallest_ascii or char_with_smallest_ascii is None:
            char_with_smallest_ascii = s[i]
    return char_with_smallest_ascii
