
def filter_chars(s):
    # Create a new string with the same characters as the input string
    new_string = ""
    for i in range(len(s)):
        # Check if the current character is between indices 69 and 97 (both exclusive)
        if 69 < s[i] < 97:
            # If it is, remove all occurrences of that character within the string
            new_string += s[:i] + s[i+1:]
    return new_string
