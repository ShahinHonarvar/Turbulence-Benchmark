
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string[10:15]):
        if char > 't' and char < 'v':
            new_str += string[:i] + string[i+1:]
        else:
            new_str += string[:i] + char + string[i+1:]
    return new_str
