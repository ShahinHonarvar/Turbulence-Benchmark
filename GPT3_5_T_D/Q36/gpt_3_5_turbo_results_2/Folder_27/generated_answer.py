
def filter_chars(string):
    filtered_string = ''
    for ch in string:
        if 48 < ord(ch) < 75 and ord(ch) > ord('6') and ord(ch) < ord('_'):
            continue
        filtered_string += ch
    return filtered_string
