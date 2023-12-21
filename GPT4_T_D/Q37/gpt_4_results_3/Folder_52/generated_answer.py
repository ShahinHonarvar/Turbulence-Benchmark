
def filter_chars(str):
    replace_chars = [char for char in str[54:84] if 'j' <= char <= 'v']
    for char in replace_chars:
        str = str.replace(char, '')
    return str
