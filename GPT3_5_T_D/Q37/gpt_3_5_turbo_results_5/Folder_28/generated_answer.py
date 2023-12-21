
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 20 <= i <= 79 and '!' <= string[i] <= 'T':
            continue
        filtered_string += string[i]
    return filtered_string
