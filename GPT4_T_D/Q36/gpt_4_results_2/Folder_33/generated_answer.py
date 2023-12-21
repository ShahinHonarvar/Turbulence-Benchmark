
def filter_chars(string):
    for i in range(300, 418):
        if i < len(string) and '9' < string[i] < 'P':
            string = string.replace(string[i], "")
    return string
