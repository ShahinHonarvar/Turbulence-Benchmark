
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for char in s:
        # If the current character is between indices 41 and 64, both inclusive,
        # and is greater than or equal to character 'K' and smaller than or equal to character ']',
        # then remove all occurrences of that character from the input string.
        if 41 <= ord(char) <= 64 and char >= "K" and char <= "]":
            filtered += char * 0

    return filtered
