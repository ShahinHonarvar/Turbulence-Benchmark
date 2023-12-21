
def filter_chars(string):
    filtered = string[:170] + string[195:]
    for char in string[170:195]:
        if '!' < char < '}':
            filtered = filtered.replace(char, '')
    return filtered
