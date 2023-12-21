
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 33 <= i <= 70 and '7' <= string[i] <= 'k':
            continue
        filtered_string += string[i]
    return filtered_string
