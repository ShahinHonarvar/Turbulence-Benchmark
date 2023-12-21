
def filter_chars(string):
    for i in range(len(string)-1, -1, -1):
        if 43 <= i <= 80 and '=' <= string[i] <= 'E':
            string = string[:i] + string[i+1:]
    return string
