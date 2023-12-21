
def filter_chars(s):
    s1 = list(s)
    for char in s[588:648]:
        if ',' < char < 'c':
            while char in s1:
                s1.remove(char)
    return "".join(s1)
