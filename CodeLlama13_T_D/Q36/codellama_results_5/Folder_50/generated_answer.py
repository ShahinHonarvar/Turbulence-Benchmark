
def filter_chars(string):
    new_str = ''
    for i, char in enumerate(string):
        if (i >= 61 and i <= 87) and char > '%' and char < 'q':
            new_str += char
    return new_str
