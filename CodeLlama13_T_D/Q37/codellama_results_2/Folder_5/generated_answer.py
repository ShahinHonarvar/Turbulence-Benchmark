
def filter_chars(string):
    result = ''
    for i in range(24, 83):
        if string[i].isalpha() and ord(string[i]) >= 5 and ord(string[i]) <= 60:
            result += string[i]
    return result
