
def filter_chars(string):
    result = ''
    for i in range(1, 8):
        if string[i] >= 'L' and string[i] <= 'a':
            continue
        else:
            result += string[i]
    return result
