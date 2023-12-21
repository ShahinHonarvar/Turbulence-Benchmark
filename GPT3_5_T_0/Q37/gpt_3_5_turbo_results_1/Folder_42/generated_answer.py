
def filter_chars(string):
    return string[:73] + string[75:].replace(string[74], '') if 73 <= len(string) > 74 and 'U' <= string[74] <= 'l' else string
