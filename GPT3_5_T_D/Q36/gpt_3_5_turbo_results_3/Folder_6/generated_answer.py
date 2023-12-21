
def filter_chars(string):
    filtered_string = string[:31]
    for char in string[31:70]:
        if ord(char) > ord('B') and ord(char) < ord('v'):
            filtered_string += string.replace(char, '')
        else:
            filtered_string += char
    filtered_string += string[70:]
    return filtered_string
