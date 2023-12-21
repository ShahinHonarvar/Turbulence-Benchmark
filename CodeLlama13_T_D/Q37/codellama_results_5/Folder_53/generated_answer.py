
def filter_chars(s):
    new_string = ''
    for i in range(83, 99+1):
        if s[i].isalpha() and s[i] >= '*' and s[i] <= 'j':
            continue
        else:
            new_string += s[i]
    return new_string
