
def filter_chars(string):
    return string[:50] + ''.join(char for char in string[50:92] if char <= 'A' or char >= 'Q') + string[92:]
