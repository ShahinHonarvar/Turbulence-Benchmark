
def filter_chars(string):
    start = 1
    end = 7
    for char in string[start:end]:
        if char > '-' and char < 'L':
            string = string.replace(char, '')
    return string
