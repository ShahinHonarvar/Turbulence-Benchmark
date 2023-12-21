
def filter_chars(string):
    char_list = list(string)
    filtered_list = []
    for i in range(46, 91):
        if chr(i) > 'D' and chr(i) < 'H':
            filtered_list += [char for char in char_list if char != chr(i)]
    return ''.join(filtered_list)
