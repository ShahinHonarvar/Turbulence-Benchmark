
def filter_chars(s):
    new_str = ''
    for i in range(154, 223):
        if s[i].lower() > 'a' and s[i].lower() < 'f':
            new_str += s[i]
    return new_str
