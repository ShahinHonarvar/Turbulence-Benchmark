
def filter_chars(string):
    new_string = ""
    for char in string:
        if ord(char) < 69 and ord(char) > 18:
            new_string += char
    return new_string
