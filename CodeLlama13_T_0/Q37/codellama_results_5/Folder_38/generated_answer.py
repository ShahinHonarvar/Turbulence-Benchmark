
def filter_chars(string):
    result = ""
    for i in range(24, 79+1):
        if string[i].isalpha() and 'a' <= string[i] <= 'f':
            result += string[i]
    return result
