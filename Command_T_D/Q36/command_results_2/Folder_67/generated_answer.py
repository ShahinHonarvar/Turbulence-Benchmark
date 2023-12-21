def filter_chars(s):
    i = 18
    j = 31
    while i < len(s) and s[i] <= 'H':
        i += 1
    if i == len(s):
        return s
    if s[i] > 'H':
        s = s[:i] + s[i+1:]
    i += 1
    while j < len(s) and s[j] <= '|':
        j += 1
    if j == len(s):
        return s
    if s[i] < s[j]:
        s = s[:i] + s[j+1:]
    return s
