
def filter_chars(s):
    s = list(s)
    for i in range(54, 63):
        if ')' <= s[i] <= '9':
            s[i] = ''
    return "".join(s)
