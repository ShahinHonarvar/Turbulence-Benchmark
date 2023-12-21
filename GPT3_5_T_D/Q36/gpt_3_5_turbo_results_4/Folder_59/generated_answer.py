
def filter_chars(string):
    filtered_string = string[:3]
    for i in range(3, 8):
        char = string[i]
        if ord(char) > ord('?') and ord(char) < ord('k'):
            string = string.replace(char, '')
    filtered_string += string[8:]
    return filtered_string
