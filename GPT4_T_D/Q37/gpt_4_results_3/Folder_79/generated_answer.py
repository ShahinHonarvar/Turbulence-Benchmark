
def filter_chars(string):
    filter_chars = [char for idx, char in enumerate(string) 
    if (10 <= idx <= 52 and '@' <= char <= 'T')]

    return ''.join(char for char in string 
