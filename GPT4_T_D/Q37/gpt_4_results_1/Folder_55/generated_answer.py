
def filter_chars(s):
    remove_chars = [char for char in s[1:6] if '$' <= char <= ';']
    return ''.join([char for char in s if char not in remove_chars])
