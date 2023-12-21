
def filter_chars(string):
    return string[:43] + string[43:83].replace(':', '').replace('Q', '') + string[83:]
