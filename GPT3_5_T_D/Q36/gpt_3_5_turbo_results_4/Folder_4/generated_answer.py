
def filter_chars(string):
    return string[:42] + ''.join([char for char in string[42:67] if not ('6' < char < 'g')]) + string[67:]
