
def filter_chars(string):
    result = ""
    for i in range(18, 95):
        if string[i].isalpha() and string[i] > 'K' and string[i] < 'a':
            result += string[i]
    return result
