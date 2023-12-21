
def filter_chars(string):
    for char in string[36:80]:
        if 'a' <= char <= 'i':
            string = string.replace(char, "")
    return string
