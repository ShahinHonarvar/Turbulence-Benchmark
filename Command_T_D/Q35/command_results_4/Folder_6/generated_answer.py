def remove_repeat_chars(s):
    return "".join(x for x in s if s.count(x) == 1)
