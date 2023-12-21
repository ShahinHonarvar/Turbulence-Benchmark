
def remove_repeat_chars(strn):
    repeat_chars = [c for c in strn[45:67] if strn[45:67].count(c) > 1]
    return ''.join(c for c in strn if c not in repeat_chars)
