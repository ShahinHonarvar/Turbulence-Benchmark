
def filter_chars(s):
    for char in s[27:80]:
        if '>' > char > '<':
            s = s.replace(char, '')
    return s
