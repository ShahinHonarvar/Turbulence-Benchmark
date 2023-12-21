
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if 513 <= i <= 877 and '?' <= char <= 'n'])
