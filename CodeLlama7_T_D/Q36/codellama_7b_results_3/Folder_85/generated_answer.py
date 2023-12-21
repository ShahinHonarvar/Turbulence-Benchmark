
def filter_chars(s):
    # Create a new string with all occurrences of characters between indices 55 and 80 (both exclusive) removed
    new_str = ""
    for i in range(len(s)):
        if i < 55 or i > 80:
            new_str += s[i]
    return new_str
