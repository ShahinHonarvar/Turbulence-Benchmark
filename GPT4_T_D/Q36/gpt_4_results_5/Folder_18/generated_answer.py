
def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if (i > 587 and i < 648) and char > ',' and char < 'c']
    for char in filtered_chars:
        string = string.replace(char, '')
        
    return string
