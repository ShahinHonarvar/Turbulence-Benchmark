
def filter_chars(s):
    chars_to_remove = set()
    for i in range(12, min(26, len(s))):
        if 'P' <= s[i] <= 'x':
            chars_to_remove.add(s[i])
    return ''.join([char for char in s if char not in chars_to_remove])
