
def filter_chars(string):
    return string[:15] + ''.join([c for c in string[15:56] if not ('W' <= c <= '{')]) + string[56:]
