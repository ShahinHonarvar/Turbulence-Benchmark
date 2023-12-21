
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 227 <= i <= 235 and 'D' <= string[i] <= 'u':
            continue
        filtered_string += string[i]
    return filtered_string
