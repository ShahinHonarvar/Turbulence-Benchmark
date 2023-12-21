
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set(s)
    # Iterate over each character in the string
    for char in s:
        # If the current character is not in the set of unique characters, remove all occurrences of that character from the string
        if char not in unique_chars:
            s = s.replace(char, "")
    return s
