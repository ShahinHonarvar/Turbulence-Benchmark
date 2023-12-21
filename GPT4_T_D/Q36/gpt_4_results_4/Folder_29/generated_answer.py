
def filter_chars(string):
    filtered_chars = [char for char in string[47:68] if 'H' < char < 's']
    for char in filtered_chars:
        string = string.replace(char, '')
    return string
