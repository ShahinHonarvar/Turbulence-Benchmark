def remove_repeat_chars(s):
    return "".join(c for c in s if s.count(c) == 1)
