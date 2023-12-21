
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for char in s:
        # If the character is between indices 19 and 32, inclusive,
        # and is greater than or equal to 'f' and smaller than or equal to 'o',
        # then remove all occurrences of that character from the filtered string.
        if 19 <= s.index(char) <= 32 and char >= 'f' and char <= 'o':
            filtered = filtered.replace(char, "")

    return filtered
