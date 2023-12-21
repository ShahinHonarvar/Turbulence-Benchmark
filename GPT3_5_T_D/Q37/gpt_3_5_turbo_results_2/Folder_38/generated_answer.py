
def filter_chars(string):
    filtered_chars = ''
    for i in range(len(string)):
        if 24 <= i <= 79 and 'a' <= string[i] <= 'f':
            continue
        filtered_chars += string[i]
    return filtered_chars
