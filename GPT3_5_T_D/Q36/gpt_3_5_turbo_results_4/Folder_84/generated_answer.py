
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 171 <= i < 636:
            if 'c' < string[i] < 's':
                continue
        filtered_string += string[i]
    return filtered_string
