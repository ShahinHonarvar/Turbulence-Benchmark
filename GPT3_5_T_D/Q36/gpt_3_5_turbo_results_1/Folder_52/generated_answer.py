
def filter_chars(string):
    return string[:49] + string[49:56].replace('I', '').replace('a', '') + string[56:]
