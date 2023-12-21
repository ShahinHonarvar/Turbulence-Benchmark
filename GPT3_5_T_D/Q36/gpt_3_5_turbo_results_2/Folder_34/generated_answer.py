
def filter_chars(string):
    filtered_string = string[:10]
    for char in string[10:79]:
        if ord(char) > ord('?') and ord(char) < ord('m'):
            filtered_string += string.replace(char, '')
    filtered_string += string[79:]
    return filtered_string
