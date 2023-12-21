
def remove_repeat_chars(string):
    # Create a set of unique characters in the string
    unique_chars = set(string)
    # Iterate over each character in the string and check if it occurs more than once between indices 70 and 200
    for char in unique_chars:
        # Check if the current character occurs more than once between indices 70 and 200
        if string.count(char) > 1 and (string.index(char) > 70 and string.rindex(char) < 200)):
            # Replace all occurrences of the current character with an empty string
            string = string.replace(char, "")
    return string
