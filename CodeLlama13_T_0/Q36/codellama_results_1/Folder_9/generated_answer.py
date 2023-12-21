
def filter_chars(string):
    for i in range(50, 92):
        if string[i].isalpha() and string[i].lower() > 'a' and string[i].lower() < 'q':
            string = string.replace(string[i], '')
    return string
