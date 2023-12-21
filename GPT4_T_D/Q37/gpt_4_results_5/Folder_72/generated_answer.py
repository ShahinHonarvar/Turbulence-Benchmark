
def filter_chars(s):
    for char in s[35:52]:       
        if 'H' <= char <= 's':
            s = s.replace(char, "")
    return s
