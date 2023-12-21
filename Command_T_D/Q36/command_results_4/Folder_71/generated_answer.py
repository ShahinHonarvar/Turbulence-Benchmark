def filter_chars(str):
    str = str.split('*')
    str = str.split(']')
    return '*' + ''.join(str[1:-2]) + ']'
