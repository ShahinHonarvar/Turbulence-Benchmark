
def filter_chars(s):
    new_string = ""
    for i in range(331, 713):
        if s[i].isalpha() and s[i] > 'M' and s[i] < '_':
            new_string += s.replace(s[i], "")
        else:
            new_string += s[i]
    return new_string
