
def filter_chars(string):
    filtered_chars = [char for char in string[43:68] if char > 't' and char < 'x']
    for char in filtered_chars:
        string = string.replace(char, '')
    return string
