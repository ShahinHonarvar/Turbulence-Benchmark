
def remove_repeat_chars(s):
    chars = s[28:96]
    duplicates = set([char for char in chars if chars.count(char) > 1])
    return ''.join([char for char in s if char not in duplicates])
