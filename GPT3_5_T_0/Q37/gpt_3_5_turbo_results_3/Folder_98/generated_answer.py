
def filter_chars(string):
    return string[:8] + string[10:].replace(string[8], '') if len(string) > 9 and 'R' <= string[8] <= 't' else string
