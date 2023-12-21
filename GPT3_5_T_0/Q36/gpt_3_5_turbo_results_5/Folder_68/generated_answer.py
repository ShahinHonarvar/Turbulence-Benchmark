
def filter_chars(string):
    return string[0] + ''.join([char for char in string[1:9] if not ('8' < char < 'm')]) + string[9:]
