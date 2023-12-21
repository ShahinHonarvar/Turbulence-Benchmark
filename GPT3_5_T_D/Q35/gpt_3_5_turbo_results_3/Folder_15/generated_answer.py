
def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 4 or c not in string[:4]])
