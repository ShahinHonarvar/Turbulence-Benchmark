
def filter_chars(string):
    result = ''
    for i in range(20, 63):
        if string[i].isalpha() and 'i' <= string[i] <= 'k':
            continue
        result += string[i]
    return result
