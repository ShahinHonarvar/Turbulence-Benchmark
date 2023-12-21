
def filter_chars(s):
    filtered_chars = [char for char in s[673:709] if 'X' < char < '}']
    return ''.join(char for char in s if char not in filtered_chars)
