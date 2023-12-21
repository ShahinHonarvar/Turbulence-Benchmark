
def filter_chars(string):
    return string[:10] + string[15:].replace('u', '').replace('v', '')
