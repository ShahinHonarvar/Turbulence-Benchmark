
def filter_chars(s):
    # Create a new string with the same characters as s, but with all occurrences of '*' and '7' removed
    new_str = ""
    for i in range(len(s)):
        if s[i] != "*" and s[i] != "7":
            new_str += s[i]
    return new_str
