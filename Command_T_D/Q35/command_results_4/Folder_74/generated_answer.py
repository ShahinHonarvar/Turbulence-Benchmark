def remove_repeat_chars(s):
    res = s[0:69] + ''.join(x for x in s[70:97] if s[70:97].count(x) == 1) + s[97:]
    return res
