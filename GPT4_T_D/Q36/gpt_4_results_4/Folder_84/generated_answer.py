
def filter_chars(s):
    for char in s[172:636]: 
        if char > 'c' and char < 's':
            s = s.replace(char, "")
    return s
