
def filter_chars(s):
    # Create a new string with all occurrences of '$' and '?' removed
    result = ''
    for i in range(len(s)):
        if s[i] != '$' and s[i] != '?':
            result += s[i]
    return result
