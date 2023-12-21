
def filter_chars(string):
    for i in range(343, 665):
        if string[i] > '%' and string[i] < 'U':
            string = string[:i] + string[i+1:]
    return string
