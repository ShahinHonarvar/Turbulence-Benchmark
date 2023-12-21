
def filter_chars(string):
    return string[:61] + ''.join(c for c in string[61:88] if c <= '%' or c >= 'q') + string[88:]
