
def filter_chars(string):
    return string[:283] + ''.join([i for i in string[283:484] if i <= 'l' or i >= 't']) + string[484:]
