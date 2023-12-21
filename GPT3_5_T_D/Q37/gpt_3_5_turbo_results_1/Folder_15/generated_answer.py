
def filter_chars(string):
    return ''.join([c for i,c in enumerate(string) if i < 2 or i > 6 or not ('?'<= c <= 'f')])
