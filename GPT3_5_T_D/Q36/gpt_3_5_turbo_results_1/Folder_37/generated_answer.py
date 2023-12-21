
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if 44 <= ord(char) < 59 and '/' < char < '6':
            continue
        filtered_string += char
    return filtered_string
