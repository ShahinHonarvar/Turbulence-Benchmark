
def filter_chars(string):
    return string[:11] + ''.join([c for c in string[11:73] if c < 'i' or c > 'v']) + string[73:]
