
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 124 <= i <= 854 and '9' <= string[i] <= 's':
            continue
        filtered_string += string[i]
    return filtered_string
