
def filter_chars(string):
    filtered_string = string[:476]
    for char in string[476:948]:
        if char > 'b' and char < 'd':
            filtered_string += string.replace(char, '')
    filtered_string += string[948:]
    return filtered_string
