
def filter_chars(string):
    result = ''
    for i in range(18, 95):
        char = string[i]
        if char > 'K' and char < 'a':
            continue
        else:
            result += char
    return result
