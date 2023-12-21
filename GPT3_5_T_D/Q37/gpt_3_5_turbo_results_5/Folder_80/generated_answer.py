
def filter_chars(string):
    return string[:36] + ''.join([char for char in string[36:80] if char < 'a' or char > 'i']) + string[80:]
