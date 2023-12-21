
def filter_chars(s):
    temp = list(s)
    for ch in temp[20:69]:
        if '<' < ch < 'C':
            s = s.replace(ch,'')
    return s
