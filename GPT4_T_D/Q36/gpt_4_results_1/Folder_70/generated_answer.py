
def filter_chars(str):
    chars_to_remove = [c for c in str[171:195] if '!' < c < '}']
    for char in chars_to_remove:
        str = str.replace(char, '')
    return str
