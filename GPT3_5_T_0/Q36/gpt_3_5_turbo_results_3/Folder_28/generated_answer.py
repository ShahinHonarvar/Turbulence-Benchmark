
def filter_chars(string):
    return string[:31] + ''.join([char for char in string[31:73] if not ('M' < char < 'j')]) + string[73:]
