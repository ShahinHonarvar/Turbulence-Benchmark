
def filter_chars(s):
    filtered = ""
    for i, char in enumerate(s):
        if 73 <= i <= 74 and 'U' <= char <= 'l':
            s = s.replace(char, "")
        filtered += s[i]
    return filtered
