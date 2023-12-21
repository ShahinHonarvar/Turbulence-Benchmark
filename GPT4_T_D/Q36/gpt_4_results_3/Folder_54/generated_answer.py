
def filter_chars(string):
    targets = [char for char in string[19:38] if char > ')' and char < 'P']
    return ''.join(char for char in string if char not in targets)
