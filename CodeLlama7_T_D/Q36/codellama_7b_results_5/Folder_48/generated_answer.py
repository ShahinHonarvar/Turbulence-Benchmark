
def filter_chars(s):
    # Remove all occurrences of characters between indices 154 and 222 (both exclusive) that are greater than character 'A' and smaller than character 'f'
    for i in range(len(s)):
        if 154 < i < 222:
            if s[i] > 'A' and s[i] < 'f':
                s = s[:i] + s[i+1:]
    return s
