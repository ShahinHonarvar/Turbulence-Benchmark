
def filter_chars(string):
    filtered_chars = ''
    for i in range(len(string)):
        if i < 19 or i > 22 or string[i] < ']' or string[i] > 't':
            filtered_chars += string[i]
    return filtered_chars
