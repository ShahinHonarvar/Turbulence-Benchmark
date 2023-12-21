
def filter_chars(string):
    start = 221
    end = 419
    filtered_string = ''
    for i, char in enumerate(string):
        if start <= i < end and '-' < char < 'v':
            continue
        filtered_string += char
    return filtered_string
