
def filter_chars(string):
    return string[:50] + ''.join([char for char in string[50:92] if not 'A' < char < 'Q']) + string[92:]
