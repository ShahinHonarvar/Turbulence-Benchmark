
def filter_chars(string):
    for i in range(29, 34):
        if string[i].isalpha():
            string = string.replace(string[i], '')
    return string
