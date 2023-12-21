
def filter_chars(string):
    for i in range(18, 31):
        if string[i] > 'H' and string[i] < '|':
            string = string[:i] + string[i+1:]
    return string
