
def filter_chars(s):
    new_string = ''
    for i, c in enumerate(s):
        if (163 <= ord(c) <= 658 and c not in '[]') or (i < 163 or i > 658):
            new_string += c
    return new_string
