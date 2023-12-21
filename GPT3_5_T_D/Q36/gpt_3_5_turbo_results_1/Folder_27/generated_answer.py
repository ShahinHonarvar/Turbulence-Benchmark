
def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i >= 48 and i < 75:
            if string[i] > '6' and string[i] < '_':
                continue
        result += string[i]
    return result
