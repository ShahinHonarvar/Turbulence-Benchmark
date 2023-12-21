
def remove_repeat_chars(s):
    # Create a new string that stores the modified characters
    new_str = ""
    # Iterate through each character in the given string
    for i in range(len(s)):
        # Check if the current character occurs more than once between indices 32 and 99
        if s.count(s[i]) > 1 and i >= 32 and i < 99:
            # Remove all occurrences of the current character from the string
            new_str += s[:i] + s[i+1:]
    return new_str
