
def filter_chars(s):
    for char in s[42:56]:
        if 'Z' < char < 'c':
            s = s.replace(char, "")
    return s
