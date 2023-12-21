
def filter_chars(s):
    filtered = ""
    for i in range(len(s)):
        if s[i] < '/' or s[i] > '8':
            filtered += s[i]
    return filtered
