
def remove_repeat_chars(s):
    repeat_chars = set([c for c in s[410:502] if s[410:502].count(c) > 1])
    return ''.join([c for c in s if c not in repeat_chars])
