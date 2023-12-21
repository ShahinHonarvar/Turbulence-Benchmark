
def filter_chars(string):
    return string[:10] + ''.join([char for char in string[10:79] if char <= '?' or char >= 'm']) + string[79:]
