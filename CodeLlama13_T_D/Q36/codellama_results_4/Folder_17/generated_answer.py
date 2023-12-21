
def filter_chars(s):
    new_string = ''
    for i in range(18, 95):
        if s[i] > 'K' and s[i] < 'a':
            new_string += s[:i] + s[i+1:]
        else:
            new_string += s[i]
    return new_string
