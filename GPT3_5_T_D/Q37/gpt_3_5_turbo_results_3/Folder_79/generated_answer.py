
def filter_chars(string):
    return string[:10] + ''.join([char for char in string[10:52] if '@' > char or char > 'T']) + string[52:]
