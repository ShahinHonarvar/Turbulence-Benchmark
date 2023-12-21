
def filter_chars(string):
    filtered_chars = set([c for c in string[72:95] if '.' <= c <= 'b'])
    for char in filtered_chars:
        string = string.replace(char, '')
    return string
