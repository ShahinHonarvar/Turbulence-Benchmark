
def filter_chars(string):
    filtered_str = ''
    for i in range(len(string)):
        if 36 <= i <= 79 and '2' <= string[i] <= 's':
            continue
        filtered_str += string[i]
    return filtered_str
