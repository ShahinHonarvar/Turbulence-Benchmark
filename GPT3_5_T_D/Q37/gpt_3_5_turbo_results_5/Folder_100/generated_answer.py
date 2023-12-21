
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 88 and i <= 90 and 'J' <= string[i] <= 'Q':
            continue
        filtered_string += string[i]
    return filtered_string
