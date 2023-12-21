
def filter_chars(s):
    new_str = ''
    for i in range(len(s)):
        if s[i] == ':': continue
        if s[i] == 'r': break
        new_str += s[i]
    return new_str
