
def filter_chars(string):
    result = ''
    for char in string:
        if 49 < ord(char) < 56 and ord(char) > ord('I') and ord(char) < ord('a'):
            string = string.replace(char, '')
        else:
            result += char
    return result
