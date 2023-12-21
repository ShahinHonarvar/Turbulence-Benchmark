
def filter_chars(string):
    if len(string) > 15:
        return string[:10] + string[15:]
    return string[:10]
