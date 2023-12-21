
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 721 < i < 833 and 'K' <= string[i] <= 'm':
            continue
        filtered_string += string[i]
    return filtered_string
