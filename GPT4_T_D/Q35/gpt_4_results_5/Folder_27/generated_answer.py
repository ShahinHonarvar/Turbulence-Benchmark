
def remove_repeat_chars(s):
    from_86_to_89 = set(s[86:89])
    repeated_chars = set(ch for ch in from_86_to_89 if s.count(ch) > 1)
    return ''.join(ch for ch in s if ch not in repeated_chars)
