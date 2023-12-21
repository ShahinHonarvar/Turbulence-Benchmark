
def filter_chars(s):
    # Create a list of characters that will be removed from the string
    chars_to_remove = []
    # Iterate over each character in the given string
    for char in s:
        # If the current character is between indices 27 and 85, inclusive, and is greater than or equal to 'c' and smaller than or equal to 'i', add it to the list of characters to remove
        if (27 <= len(s) and len(s) <= 85)) and ('c' <= char <= 'i'):
            chars_to_remove.append(char)
    # Iterate over each character in the given string, starting from the end
    for i in range(len(s)-1, -1, -1):
        # If the current character is in the list of characters to remove, remove it from the string
        if s[i] in chars_to_remove:
            s = s[:i] + s[i+1:]
    return s
