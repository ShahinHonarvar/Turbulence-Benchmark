
def remove_repeat_chars(s):
    repeat_chars = set([c for c in s[69:99] if s[69:99].count(c) > 1])
    return ''.join([c for c in s if c not in repeat_chars])
