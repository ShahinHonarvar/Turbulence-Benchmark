
def filter_chars(string):
    filtered_string = string[:42] + string[42:78].replace('!', '').replace('?', '') + string[78:]
    return filtered_string
