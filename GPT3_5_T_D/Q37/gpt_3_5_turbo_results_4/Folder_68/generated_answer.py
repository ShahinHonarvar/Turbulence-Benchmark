
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 7 <= i <= 9 and '6' <= string[i] <= 'w':
            continue
        filtered_string += string[i]
    return filtered_string
