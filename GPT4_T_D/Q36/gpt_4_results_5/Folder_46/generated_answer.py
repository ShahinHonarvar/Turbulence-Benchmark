
def filter_chars(str):
    chars_to_remove = [char for char in str[20:69] if '<' < char < 'C']
    for char in chars_to_remove:
        str = str.replace(char, '')
    return str
