
def filter_chars(string):
    new_str = ""
    for char in string:
        if ord(char) >= 155 and ord(char) <= 403 and (char >= '(' and char <= ']'):
            continue
        new_str += char
    return new_str
