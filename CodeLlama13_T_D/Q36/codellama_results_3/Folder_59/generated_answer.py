
def filter_chars(s):
    # Loop through all characters in s, except for the first three and last eight
    for i in range(3, len(s) - 8):
        # If the current character is between '?' and 'k', remove it from the string
        if s[i] > '?' and s[i] < 'k':
            s = s.replace(s[i], '')
    return s
