
def filter_chars(string):
    new_string = ""
    for char in string:
        if 66 < ord(char) < 90 and char > '#' and char < 'T':
            continue
        new_string += char
    return new_string
