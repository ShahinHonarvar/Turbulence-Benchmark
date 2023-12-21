
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 12 <= index <= 77 and ':' <= char <= 'L':
            string = string.replace(char, '')
    return string
