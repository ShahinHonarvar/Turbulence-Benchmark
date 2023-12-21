
def filter_chars(string):
    return string[:54] + ''.join([c for c in string[54:92] if c > 'J' and c < 'X']) + string[92:]
