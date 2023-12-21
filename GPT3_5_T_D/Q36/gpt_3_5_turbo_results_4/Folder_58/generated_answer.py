
def filter_chars(string):
    return string[:318] + ''.join(char for char in string[318:337] if not ('B' < char < 'z')) + string[337:]
