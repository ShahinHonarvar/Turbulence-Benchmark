
def filter_chars(string):
    if len(string) < 9:
        return string
    else:
        return string[:3] + string[9:] if '*' < string[3:4] < 'E' else string[:3] + string[3:9].replace(string[3:4], '') + string[9:]
