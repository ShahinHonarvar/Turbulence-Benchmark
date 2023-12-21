
def remove_repeat_chars(string):
    for i in range(60, 200):
        if string.count(string[i]) > 1:
            string = string.replace(string[i], '')
    return string
