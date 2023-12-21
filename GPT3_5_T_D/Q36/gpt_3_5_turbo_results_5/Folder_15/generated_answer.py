
def filter_chars(string):
    return string[:2] + "".join([char for char in string[2:7] if not ('h' < char < 'k')]) + string[7:]
