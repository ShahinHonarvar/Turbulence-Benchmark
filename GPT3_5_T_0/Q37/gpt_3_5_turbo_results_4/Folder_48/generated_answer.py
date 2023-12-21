
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 513 or i > 877 or char < '?' or char > 'n'])
