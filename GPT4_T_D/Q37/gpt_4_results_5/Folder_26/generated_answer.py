
def filter_chars(str):
    chars = set(str[20:63])
    for char in chars:
        if 'i' <= char <= 'k':
            str = str.replace(char, '')
    return str
