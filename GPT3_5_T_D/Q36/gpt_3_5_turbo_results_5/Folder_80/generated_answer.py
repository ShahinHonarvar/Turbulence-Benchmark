
def filter_chars(string):
    start = 54
    end = 92
    new_string = string[:start] + string[end:]
    for i in range(start, end):
        if 'J' < string[i] < 'X':
            new_string = new_string.replace(string[i], '')
    return new_string
