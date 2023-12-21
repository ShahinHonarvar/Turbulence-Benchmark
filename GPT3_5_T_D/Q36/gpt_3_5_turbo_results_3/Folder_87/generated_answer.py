
def filter_chars(string):
    new_string = ""
    for char in string:
        if 32 < ord(char) < 61 and 'D' > char > '3':
            continue
        new_string += char
    return new_string
