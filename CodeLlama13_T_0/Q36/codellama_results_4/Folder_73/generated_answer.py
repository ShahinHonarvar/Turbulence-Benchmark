
def filter_chars(string):
    new_string = ""
    for char in string:
        if ord(char) < 66 or ord(char) > 90:
            new_string += char
    return new_string
