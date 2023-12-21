
def filter_chars(string):
    return string[:42] + string[42:78].replace('!', '').replace('?', '') + string[78:]
