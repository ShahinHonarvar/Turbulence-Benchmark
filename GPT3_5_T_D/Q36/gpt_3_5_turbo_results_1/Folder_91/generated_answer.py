
def filter_chars(string):
    for i in range(3):
        if '$' < string[i] < '?':
            string = string.replace(string[i],'')
    return string
