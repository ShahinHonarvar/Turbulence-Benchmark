
def filter_chars(string):
    return string[:38] + ''.join([char for char in string[38:70] if not ('H' <= char <= 'e')]) + string[70:]
