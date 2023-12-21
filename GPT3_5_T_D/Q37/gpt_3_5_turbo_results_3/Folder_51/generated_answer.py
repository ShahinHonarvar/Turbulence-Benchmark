
def filter_chars(string):
    chars_to_remove = set(string[36:41]) & set("Hijklmnopqrstudefg")
    return ''.join(char for char in string if char not in chars_to_remove)
