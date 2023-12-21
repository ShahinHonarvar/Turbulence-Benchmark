
def remove_repeat_chars(s):
    char_list = list(s)
    substr = char_list[43:87]
    char_set = set(substr)
    for c in char_set:
        if substr.count(c) > 1:
            s = s.replace(c, '')
    return s
