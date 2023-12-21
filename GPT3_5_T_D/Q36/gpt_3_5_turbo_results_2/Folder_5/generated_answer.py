
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 55 <= i < 66:
            if 'f' < string[i] < '|':
                continue
        filtered_string += string[i]
    return filtered_string
