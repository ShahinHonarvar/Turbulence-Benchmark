
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if ord(char) > 586 and ord(char) < 649:
            filtered_string += char
        else:
            filtered_string += char
    return filtered_string
