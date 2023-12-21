
def filter_chars(string):
    return string[:52] + ''.join([c for c in string[52:82] if 'A' > c or c > 'U']) + string[82:]
