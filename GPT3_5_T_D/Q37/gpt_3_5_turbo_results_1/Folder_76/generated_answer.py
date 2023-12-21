
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if i >= 379 and i <= 898 and string[i] >= 'M' and string[i] <= 'v':
            continue
        result += string[i]
    return result
