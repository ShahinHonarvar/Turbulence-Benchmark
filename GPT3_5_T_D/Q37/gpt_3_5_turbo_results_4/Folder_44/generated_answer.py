
def filter_chars(string):
    for i in range(21, 44):
        if '+' <= string[i] <= '8':
            string = string.replace(string[i], '')
    return string
