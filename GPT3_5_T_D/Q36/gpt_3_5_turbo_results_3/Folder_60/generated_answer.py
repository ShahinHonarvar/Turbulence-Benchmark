
def filter_chars(string):
    filtered_string = string[:23] + string[83:]
    for char in string[23:83]:
        if 'f' < char < 'o':
            filtered_string = filtered_string.replace(char, '')
    return filtered_string
