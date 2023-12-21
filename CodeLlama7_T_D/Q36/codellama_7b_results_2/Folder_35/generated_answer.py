
def filter_chars(s):
    # Create a new string with the same characters as s, but without any occurrences of '(' or ']'
    filtered = ''
    for i in range(len(s)):
        if s[i] != '(' and s[i] != ']':
            filtered += s[i]
    return filtered
