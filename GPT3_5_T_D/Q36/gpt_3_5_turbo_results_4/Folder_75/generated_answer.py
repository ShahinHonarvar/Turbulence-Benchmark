
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 46 <= i < 74 and '&' < string[i] < 'M':
            continue
        filtered_string += string[i]
    return filtered_string
