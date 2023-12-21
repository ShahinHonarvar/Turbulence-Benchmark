
def filter_chars(s):
    removed_chars = [char for char in s[91:97] if 'j' < char < 'w']
    return ''.join([char for char in s if char not in removed_chars])
