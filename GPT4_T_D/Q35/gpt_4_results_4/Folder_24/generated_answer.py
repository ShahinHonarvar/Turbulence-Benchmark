
def remove_repeat_chars(s):
    s = list(s)
    s[14:91] = "".join(i for i in set(s[14:91]))
    return "".join(s)
