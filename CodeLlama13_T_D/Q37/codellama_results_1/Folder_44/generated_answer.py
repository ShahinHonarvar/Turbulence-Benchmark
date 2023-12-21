
def filter_chars(string):
    result = ''
    for i in range(21, 44):
        if string[i].isdigit() and '+' <= string[i] <= '8':
            continue
        else:
            result += string[i]
    return result
