
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if i < 41 or i > 86:
            result += string[i]
        elif string[i] >= 'S' and string[i] <= 's':
            continue
        else:
            result += string[i]
    return result
