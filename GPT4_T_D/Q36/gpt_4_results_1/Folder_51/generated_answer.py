
def filter_chars(s):
    substr = s[59:81]
    for char in substr:
        if '5' < char < '>':
            s = s.replace(char, "")
    return s
