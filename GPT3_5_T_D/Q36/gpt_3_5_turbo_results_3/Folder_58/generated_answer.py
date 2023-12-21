
def filter_chars(string):
    result = ''
    for char in string[:318]:
        result += char
    for char in string[318:337]:
        if char > 'B' and char < 'z':
            string = string.replace(char, '')
    for char in string[337:]:
        result += char
    return result
