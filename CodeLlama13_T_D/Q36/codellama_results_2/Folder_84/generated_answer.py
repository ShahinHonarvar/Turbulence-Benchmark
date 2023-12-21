
def filter_chars(string):
    result = ''
    for i in range(171, 636):
        if string[i] > 'c' and string[i] < 's':
            result += string[i]
    return result
