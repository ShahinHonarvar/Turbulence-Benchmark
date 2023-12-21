
def remove_repeat_chars(s):
    subset = s[44:70]
    chars_in_subset = set()
    for char in subset:
        if subset.count(char) > 1:
            chars_in_subset.add(char)
    for char in chars_in_subset:
        s = s.replace(char, '')
    return s
