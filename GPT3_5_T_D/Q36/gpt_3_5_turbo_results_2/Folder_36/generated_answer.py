
def filter_chars(string):
    return string[:283] + ''.join(char for char in string[283:484] if not ('l' < char < 't')) + string[484:]
