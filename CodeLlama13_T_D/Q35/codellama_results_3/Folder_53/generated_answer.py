
def remove_repeat_chars(string):
    for i in range(200, 203):
        if string[i] in string[200:202]:
            string = string.replace(string[i], '')
    return string
