
def filter_chars(s):
    # Create a new string with the same characters as s, but without any occurrences of t - v
    new_string = ""
    for i in range(len(s)):
        if not (s[i] > 't' and s[i] < 'v'):
            new_string += s[i]
    return new_string
