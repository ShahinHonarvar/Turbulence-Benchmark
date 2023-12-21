
def filter_chars(string):
    return string[:27] + ''.join([char for char in string[27:75] if not ('A' < char < 'i')]) + string[75:]
