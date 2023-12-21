
def filter_chars(string):
    chars_to_remove = [ch for ch in string[78:87] if ';' < ch < 'r']
    for ch in chars_to_remove:
        string = string.replace(ch, '')
    return string
