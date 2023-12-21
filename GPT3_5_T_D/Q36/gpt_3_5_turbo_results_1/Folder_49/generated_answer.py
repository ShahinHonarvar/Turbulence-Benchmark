
def filter_chars(string):
    filtered_string = string[:46]
    for c in string[46:91]:
        if c > 'D' and c < 'H':
            filtered_string = filtered_string.replace(c, '')
        else:
            filtered_string += c
    filtered_string += string[91:]
    return filtered_string
