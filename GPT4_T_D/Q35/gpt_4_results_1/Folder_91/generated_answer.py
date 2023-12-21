
def remove_repeat_chars(s):
    chars = [x for x in s[1:6] if s[1:6].count(x) > 1]
    return ''.join([x for x in s if x not in chars])
