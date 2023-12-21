
def filter_chars(string):
    string = list(string)
    remove_chars = []
    for i in range(55, 84):
        if ord(';') < ord(string[i]) < ord('z'):
            remove_chars.append(string[i])
    for char in remove_chars:
        string = [c for c in string if c != char]
    return ''.join(string)
