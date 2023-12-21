
def remove_repeat_chars(s):
    unique = set(s[39:52])
    duplicated = set(x for x in unique if s[39:52].count(x) > 1)
    return ''.join(char for char in s if char not in duplicated)
