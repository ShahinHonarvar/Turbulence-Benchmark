
def filter_chars(string):
    for index in range(83, 100):
        if '*' <= string[index] <= 'j':
            string = string.replace(string[index], "")
    return string
