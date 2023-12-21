
def filter_chars(string):
    modified_string = string[:58] + string[82:]
    for char in string[58:82]:
        if char > 'F' and char < 'O':
            modified_string = modified_string.replace(char, '')
    return modified_string
