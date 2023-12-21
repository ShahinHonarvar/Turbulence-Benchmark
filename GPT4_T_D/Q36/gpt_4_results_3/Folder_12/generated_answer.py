
def filter_chars(str):
    to_remove = [char for char in str[33:84] if 'm' < char < 'w']
    for char in set(to_remove):
        str = str.replace(char, '')
    return str
