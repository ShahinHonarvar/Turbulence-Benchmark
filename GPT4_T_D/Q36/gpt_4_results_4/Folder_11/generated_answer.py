
def filter_chars(string):
    for ch in string[87:93]:
        if 'E' < ch < '~':
            string = string.replace(ch, '')
    return string
