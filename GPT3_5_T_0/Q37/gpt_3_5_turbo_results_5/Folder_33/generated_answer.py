
def filter_chars(string):
    return string[:722] + ''.join(c for c in string[722:833] if not ('K' <= c <= 'm')) + string[833:]
