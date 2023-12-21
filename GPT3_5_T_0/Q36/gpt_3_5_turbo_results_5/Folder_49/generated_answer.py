
def filter_chars(string):
    return string[:46] + string[46:91].replace('E', '').replace('F', '').replace('G', '') + string[91:]
