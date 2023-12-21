
def filter_chars(s):
    filtered = ""
    for i in range(63, 89):
        if s[i] > '*' and s[i] < 'w':
            filtered += s[:i] + s[i+1:]
    return filtered
