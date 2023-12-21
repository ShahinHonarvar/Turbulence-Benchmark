
def filter_chars(string):
    for i in range(len(string)):
        if i >= 18 and i <= 81 and string[i] >= 'W' and string[i] <= '[':
            string = string.replace(string[i], "")
    return string
