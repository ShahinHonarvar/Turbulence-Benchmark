
def filter_chars(string):
    result = ''
    for i in range(19, 91):
        if string[i].isalpha() and string[i].lower() >= 'f' and string[i].lower() <= 'h':
            result += string[i]
    return result
