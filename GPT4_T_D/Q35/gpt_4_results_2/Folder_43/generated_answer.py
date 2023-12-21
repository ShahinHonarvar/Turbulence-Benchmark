
def remove_repeat_chars(s):
    region = s[11:28]
    repeat_chars = {char for char in region if region.count(char) > 1}
    return ''.join(char for char in s if char not in repeat_chars)
