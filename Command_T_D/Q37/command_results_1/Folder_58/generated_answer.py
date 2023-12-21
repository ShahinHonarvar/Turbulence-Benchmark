def filter_chars(str):
    new_str = ''
    for i in range(503, 753+1):
        if str[i] >= '9' and str[i] <= 'w':
            str = str.replace(str[i], '')
    new_str = str
    return new_str
