
def filter_chars(string):
    return string[:225] + ''.join(char for char in string[225:382] if char < 'D' or char > 'Y') + string[382:]
