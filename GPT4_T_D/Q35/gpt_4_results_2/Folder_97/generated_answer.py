
def remove_repeat_chars(s):
    subset = s[35:69]
    chars_to_remove = [char for char in subset if subset.count(char) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])
