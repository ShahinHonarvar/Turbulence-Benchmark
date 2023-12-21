
def filter_chars(s):
    chars_to_remove = [char for char in s[54:63] if ')' <= char <= '9']
    return ''.join([char for char in s if char not in chars_to_remove])
