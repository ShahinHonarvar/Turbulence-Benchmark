
def filter_chars(string):
    new_string = string
    for i in range(13, 29):
        if i < len(new_string) and 'c' <= new_string[i] <= 'n':
            new_string = new_string.replace(new_string[i], '')
    return new_string
