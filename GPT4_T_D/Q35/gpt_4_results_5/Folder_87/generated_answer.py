
def remove_repeat_chars(s):
    repeat_chars = [c for c in s[21:43] if s[21:43].count(c) > 1]
    result = ''.join([c for c in s if c not in repeat_chars])
    return result
