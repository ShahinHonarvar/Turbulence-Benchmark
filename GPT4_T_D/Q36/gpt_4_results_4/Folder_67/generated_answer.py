
def filter_chars(string):
    chars_to_remove = [char for char in string[19:31] if "H" < char < "|"]
    return ''.join([c for c in string if c not in chars_to_remove])
