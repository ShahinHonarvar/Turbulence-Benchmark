
def remove_repeat_chars(string):
    start = 86
    end = 89
    chars = set(string[start:end])
    return ''.join([c for c in string if c not in chars])
