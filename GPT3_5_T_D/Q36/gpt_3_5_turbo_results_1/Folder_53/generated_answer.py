
def filter_chars(string):
    new_string = ""
    for char in string:
        if 90 < ord(char) < 97 and 'j' < char < 'w':
            new_string = new_string.replace(char, '')
        else:
            new_string += char
    return new_string
