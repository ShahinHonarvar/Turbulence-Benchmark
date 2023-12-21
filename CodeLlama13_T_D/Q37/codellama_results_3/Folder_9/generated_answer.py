
def filter_chars(string):
    result = ''
    for i in range(38, 99+1):
        if string[i].isalpha() and 'A' <= string[i] <= 'Q':
            result += string[i]
    return result
