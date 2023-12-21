
def filter_chars(s):
    chars_to_remove = set()
    for i in range(19, 64):
        if s[i] > '3' and s[i] < 'B':
            chars_to_remove.add(s[i])
    res = ''.join([ch for ch in s if ch not in chars_to_remove])
    return res
