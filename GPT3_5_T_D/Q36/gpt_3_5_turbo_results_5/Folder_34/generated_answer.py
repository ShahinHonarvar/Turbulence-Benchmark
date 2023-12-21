
def filter_chars(string):
    return string[:10] + ''.join([c for c in string[10:79] if c <= '?' or c >= 'm']) + string[79:]
