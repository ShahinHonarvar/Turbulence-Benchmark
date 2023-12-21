
def filter_chars(s):
    new_str = ""
    for i in range(26, 80):
        if s[i] < '<' or s[i] > '>':
            continue
        else:
            new_str += s[i]
    return new_str
