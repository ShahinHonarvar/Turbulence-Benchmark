
def filter_chars(string):
    return string[:4] + ''.join([ch for ch in string[4:8] if ch <= '1' or ch >= 'J']) + string[8:]
