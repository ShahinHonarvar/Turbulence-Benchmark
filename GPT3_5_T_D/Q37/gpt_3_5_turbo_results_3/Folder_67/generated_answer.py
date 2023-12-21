
def filter_chars(string):
    chars_to_remove = set(string[19:23]) & set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return ''.join(char for char in string if char not in chars_to_remove)
