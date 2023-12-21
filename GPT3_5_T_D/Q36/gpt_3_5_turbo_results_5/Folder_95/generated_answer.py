
def filter_chars(string):
    return string[:56] + ''.join(char for char in string[56:86] if not '+' < char < 'w') + string[86:]
