
def filter_chars(string):
    filtered_string = string[:421] + ''.join([ch for ch in string[421:854] if not 'D' < ch < 'J']) + string[854:]
    return filtered_string
