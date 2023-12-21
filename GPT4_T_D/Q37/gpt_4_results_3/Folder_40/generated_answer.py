
def filter_chars(s):
    for i in range(len(s[:2])):
        if '*' <= s[i] <= 's':
            s = s.replace(s[i],"")
    return s
