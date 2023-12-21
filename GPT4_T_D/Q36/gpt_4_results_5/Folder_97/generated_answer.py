
def filter_chars(inp_str):
    check_range = inp_str[310:591]
    for char in check_range:
        if 'S' < char < 'm':
            inp_str = inp_str.replace(char, '')
    return inp_str
