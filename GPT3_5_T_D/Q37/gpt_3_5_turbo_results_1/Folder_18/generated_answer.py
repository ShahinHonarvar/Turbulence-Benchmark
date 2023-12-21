
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 770 or i > 970 or char < '-' or char > 'D')
