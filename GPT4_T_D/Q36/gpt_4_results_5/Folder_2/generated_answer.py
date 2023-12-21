
def filter_chars(s):
    sub_str = s[422:854]
    to_remove = []
    for char in sub_str:
        if char > 'D' and char < 'J':
            to_remove.append(char)
    for char in set(to_remove):
        s = s.replace(char, '')
    return s
