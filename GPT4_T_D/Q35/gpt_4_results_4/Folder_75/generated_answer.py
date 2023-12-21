
def remove_repeat_chars(s):
    targeted = s[21:51]
    repeated = [ch for ch in targeted if targeted.count(ch) > 1]
    return "".join([ch for ch in s if ch not in repeated])
