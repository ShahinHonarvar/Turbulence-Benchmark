
def filter_chars(string):
    return string[:502] + ''.join(char for char in string[502:946] if 'W' >= char or char >= 'y') + string[946:]
