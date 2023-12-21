
def filter_chars(string):
    return string[:299] + ''.join([c for c in string[299:418] if c <= '9' or c >= 'P']) + string[418:]
