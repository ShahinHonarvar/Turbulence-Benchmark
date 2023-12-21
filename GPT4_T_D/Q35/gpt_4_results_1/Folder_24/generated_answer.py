
def remove_repeat_chars(s):
    sublist = list(s[14:91])
    repeat_chars = [char for char in sublist if sublist.count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
