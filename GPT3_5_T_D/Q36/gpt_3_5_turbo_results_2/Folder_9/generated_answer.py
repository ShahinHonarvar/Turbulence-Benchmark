
def filter_chars(string):
    result = ''
    for char in string:
        if ord(char) > ord('A') and ord(char) < ord('Q'):
            continue
        result += char
    return result
