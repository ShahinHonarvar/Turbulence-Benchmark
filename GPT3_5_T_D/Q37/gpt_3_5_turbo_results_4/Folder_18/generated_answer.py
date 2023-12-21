
def filter_chars(string):
    return ''.join([char for index, char in enumerate(string) if index < 770 or index > 970 or char < '-' or char > 'D'])
