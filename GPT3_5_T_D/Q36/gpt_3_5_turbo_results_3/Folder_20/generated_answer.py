
def filter_chars(string):
    return string[:13] + ''.join(c for c in string[13:40] if not ('C' > c > ':')) + string[40:]
