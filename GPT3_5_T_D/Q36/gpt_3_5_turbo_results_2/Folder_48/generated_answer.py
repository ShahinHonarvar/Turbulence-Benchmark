
def filter_chars(string):
    return string[:154] + ''.join(char for char in string[154:222] if not 'A' < char < 'f') + string[222:]
