
def remove_repeat_chars(s):
    subset = s[451:905]
    repeat_chars = [char for char in subset if subset.count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
