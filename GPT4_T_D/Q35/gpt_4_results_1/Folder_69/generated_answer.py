
def remove_repeat_chars(s):
    subset = s[40:43]
    repeat_chars = [char for char in subset if subset.count(char) > 1]
    return ''.join(c for c in s if c not in repeat_chars)
