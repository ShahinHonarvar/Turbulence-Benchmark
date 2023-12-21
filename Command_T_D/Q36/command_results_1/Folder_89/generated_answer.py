def filter_chars(str):
    for i in range(57, 69):
        if str[i] > '(' and str[i] < 'W':
            str = str.replace(str[i], "")
    return str
