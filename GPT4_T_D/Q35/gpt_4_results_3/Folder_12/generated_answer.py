
def remove_repeat_chars(s):
    sub_str = s[17:87]
    to_remove = [char for char in sub_str if sub_str.count(char) > 1]
    return ''.join(c for c in s if c not in to_remove)
