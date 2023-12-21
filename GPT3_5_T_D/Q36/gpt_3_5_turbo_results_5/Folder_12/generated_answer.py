
def filter_chars(string):
    return ''.join(char for char in string if not ('m' < char < 'w')) if len(string) >= 84 else string
