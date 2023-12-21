
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if (19 <= i <= 92) and (string[i] >= '8' and string[i] <= 'm'):
            result += string[i]
        else:
            result += string[i]
    return result
