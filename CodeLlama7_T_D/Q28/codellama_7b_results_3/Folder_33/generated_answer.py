 def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string
    char_indices = {char: [] for char in string}
    for i, char in enumerate(string):
        char_indices[char].append(i)
    # Get the indices of the characters between 22 and 74
    indices = [index for index in range(22, 75)]
    # Find the character with the 12th smallest ASCII value among those characters in the string that occur between indices 22 to 74, both inclusive.
    smallest_ascii_value = None
    for i in indices:
        char = string[i]
        if smallest_ascii_value is None or smallest_ascii_value > ord(char):
            smallest_ascii_value = ord(char)
    return chr(smallest_ascii_value)
